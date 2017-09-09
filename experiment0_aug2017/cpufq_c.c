#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>

FILE *out;

char *out_path;
char *buffer;

void sig_handler(int signo) {
	if (signo == SIGINT) {
		printf("Recording to file...\n");

		sprintf(buffer + strlen(buffer), "%u\n", (unsigned)time(NULL));

		// write the observations to the provided file
		out = fopen(out_path, "w");
		fprintf(out, "%s\n", buffer);
		fclose(out);

		// free the buffer
		free(buffer);

		exit(0);
	}
}

int main(int argc, char **argv) {
	int observation;

	if (argc != 2) {
		printf("Usage: ./cpufreq <OUTPUT_FILE_PATH>\n");

		exit(1);
	}

	out_path = argv[1];

	buffer = malloc(384 * 1024);

	if (signal(SIGINT, sig_handler) == SIG_ERR)
		printf("\ncan't catch SIGINT\n");

	sprintf(buffer + strlen(buffer), "%u\n", (unsigned)time(NULL));

	// a long long wait so that we can easily issue a signal to this process
	while (1) {

		FILE *fp;
		char path[128];

		//clock_t t;
		//	t = clock();

		// open the command for reading
		fp = popen("/usr/bin/cpufreq-info | grep 'current CPU'", "r");

		if (fp == NULL) {
			printf("Failed to run command\n" );

			exit(1);
		}

		// read the output lines
		while (fgets(path, sizeof(path)-1, fp) != NULL) {
			observation = -1;
			char *scale;

			strtok(path, " ");
			strtok(NULL, " ");
			strtok(NULL, " ");
			strtok(NULL, " ");

			observation = atof(strtok(NULL, " "));
			scale = strtok(NULL, " ");
			scale = strtok(scale, ".");

			if (strcmp(scale, "GHz") == 0) {
				observation *= 1000;
			}

			sprintf(buffer + strlen(buffer), "%d\n", observation);
		}

		//t = clock() - t;
		//double time_taken = ((double)t)/CLOCKS_PER_SEC; 

		//printf("%f\n", time_taken);

		// close
		pclose(fp);

		// wait one second to fetch the information again
		sleep(1);
	}

	return 0;
}
