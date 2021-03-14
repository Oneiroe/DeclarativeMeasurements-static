# Janus Declarative Measurements
Static Repository for results and tests sharing of Janus declarative specifications measurement component.
Go to the static page to just download the files [https://github.com/Oneiroe/DeclarativeMeasurements-static](https://github.com/Oneiroe/DeclarativeMeasurements-static/tree/gh-pages)

Find the active development in the main [Janus repository](https://github.com/Oneiroe/Janus).

Janus How-to
=========================
Janus is a tool-set for the evaluation of declarative process mining specifications ([LICENSE](https://github.com/Oneiroe/MINERful/blob/master/LICENSE) here).

It is based on Linear Temporal Logic over finite traces with past operators (LTLp~f~) and specifically on the concept  of reactive constraints: formulae with an explicit distinction between the activator and consequent factors of the formula itself.

For details on the usage of the software consult the [wiki page](https://github.com/Oneiroe/Janus/wiki)

Experiments Index
=========================
* **ErrorInjectionExperiment**: Interactive HTML Plots resulting from the error injection experiment for each constraint and for each noise type (insertion, deletion, white);
* **JanusExecutable**: Janus executable used for the experiments;
* **NonDeclareRule**: logs and results for the verification of a non-DECLARE constraint. It is also provided the Janus executable enabled for "BeforeThisOrLaterThat" constraint;
* **PerformancesTests**: scripts, logs and models used to measure the time and space performance of the software;
* **RankingExperiment**: scripts and models used to perform the ranking experiment.
