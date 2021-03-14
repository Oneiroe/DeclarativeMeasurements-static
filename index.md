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
In the following are listed the files, executables and results for the experiments provided in the journal paper.

In details:
* **ErrorInjectionExperiment**: Interactive HTML Plots resulting from the error injection experiment for each constraint and for each noise type (insertion, deletion, white);
* **JanusExecutable**: Janus executable used for the experiments; 
* **NonDeclareRule**: logs and results for the verification of a non-DECLARE constraint. It is also provided the Janus executable enabled for "BeforeThisOrLaterThat" constraint;
* **PerformancesTests**: scripts, logs and models used to measure the time and space performance of the software;
* **RankingExperiment**: scripts and models used to perform the ranking experiment.


<!-- filetree -->

 - **ErrorInjectionExperiment/**
   - [ERROR-INJECTION-NEU-WHITE-NOISE-model.json](./ErrorInjectionExperiment/ERROR-INJECTION-NEU-WHITE-NOISE-model.json)
   - [ERROR-INJECTION-NEU-WHITE-NOISE.sh](./ErrorInjectionExperiment/ERROR-INJECTION-NEU-WHITE-NOISE.sh)
   - [ERROR-INJECTION-NEU-model.json](./ErrorInjectionExperiment/ERROR-INJECTION-NEU-model.json)
   - [ERROR-INJECTION-NEU.sh](./ErrorInjectionExperiment/ERROR-INJECTION-NEU.sh)
   - **ERROR-INJECTION-TASKS-INSERTION-PLOTS/**
     - [ERROR-INJECTION-a-Init(a).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-a-Init(a).html)
     - [ERROR-INJECTION-b-End(b).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-b-End(b).html)
     - [ERROR-INJECTION-c-AtMostOne(c).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-c-AtMostOne(c).html)
     - [ERROR-INJECTION-d-Participation(d).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-d-Participation(d).html)
     - [ERROR-INJECTION-e-Response(e,f).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-e-Response(e,f).html)
     - [ERROR-INJECTION-f-Response(e,f).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-f-Response(e,f).html)
     - [ERROR-INJECTION-g-Precedence(g,h).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-g-Precedence(g,h).html)
     - [ERROR-INJECTION-h-Precedence(g,h).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-h-Precedence(g,h).html)
     - [ERROR-INJECTION-i-AlternatePrecedence(i,l).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-i-AlternatePrecedence(i,l).html)
     - [ERROR-INJECTION-j-ChainSuccession(j,k).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-j-ChainSuccession(j,k).html)
     - [ERROR-INJECTION-k-ChainSuccession(j,k).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-k-ChainSuccession(j,k).html)
     - [ERROR-INJECTION-l-AlternatePrecedence(i,l).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-l-AlternatePrecedence(i,l).html)
     - [ERROR-INJECTION-m-AlternateResponse(m,n).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-m-AlternateResponse(m,n).html)
     - [ERROR-INJECTION-n-AlternateResponse(m,n).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-n-AlternateResponse(m,n).html)
     - [ERROR-INJECTION-o-ChainResponse(o,p).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-o-ChainResponse(o,p).html)
     - [ERROR-INJECTION-p-ChainResponse(o,p).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-p-ChainResponse(o,p).html)
     - [ERROR-INJECTION-q-ChainPrecedence(q,r).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-q-ChainPrecedence(q,r).html)
     - [ERROR-INJECTION-r-ChainPrecedence(q,r).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-r-ChainPrecedence(q,r).html)
     - [ERROR-INJECTION-s-RespondedExistence(s,t).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-s-RespondedExistence(s,t).html)
     - [ERROR-INJECTION-t-RespondedExistence(s,t).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-t-RespondedExistence(s,t).html)
     - [ERROR-INJECTION-u-CoExistence(u,v).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-u-CoExistence(u,v).html)
     - [ERROR-INJECTION-v-CoExistence(u,v).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-v-CoExistence(u,v).html)
     - [ERROR-INJECTION-w-Succession(w,x).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-w-Succession(w,x).html)
     - [ERROR-INJECTION-x-Succession(w,x).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-x-Succession(w,x).html)
     - [ERROR-INJECTION-y-AlternateSuccession(y,z).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-y-AlternateSuccession(y,z).html)
     - [ERROR-INJECTION-z-AlternateSuccession(y,z).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-z-AlternateSuccession(y,z).html)
     - [ERROR-INJECTION-§-NotCoExistence(ü,§).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-§-NotCoExistence(ü,§).html)
     - [ERROR-INJECTION-ü-NotCoExistence(ü,§).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-INSERTION-PLOTS/ERROR-INJECTION-ü-NotCoExistence(ü,§).html)
   - **ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/**
     - [ERROR-INJECTION-a-Init(a).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-a-Init(a).html)
     - [ERROR-INJECTION-b-End(b).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-b-End(b).html)
     - [ERROR-INJECTION-c-AtMostOne(c).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-c-AtMostOne(c).html)
     - [ERROR-INJECTION-d-Participation(d).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-d-Participation(d).html)
     - [ERROR-INJECTION-ef-Response(e,f).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-ef-Response(e,f).html)
     - [ERROR-INJECTION-gh-Precedence(g,h).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-gh-Precedence(g,h).html)
     - [ERROR-INJECTION-il-AlternatePrecedence(i,l).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-il-AlternatePrecedence(i,l).html)
     - [ERROR-INJECTION-jk-ChainSuccession(j,k).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-jk-ChainSuccession(j,k).html)
     - [ERROR-INJECTION-mn-AlternateResponse(m,n).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-mn-AlternateResponse(m,n).html)
     - [ERROR-INJECTION-op-ChainResponse(o,p).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-op-ChainResponse(o,p).html)
     - [ERROR-INJECTION-qr-ChainPrecedence(q,r).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-qr-ChainPrecedence(q,r).html)
     - [ERROR-INJECTION-st-RespondedExistence(s,t).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-st-RespondedExistence(s,t).html)
     - [ERROR-INJECTION-uv-CoExistence(u,v).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-uv-CoExistence(u,v).html)
     - [ERROR-INJECTION-wx-Succession(w,x).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-wx-Succession(w,x).html)
     - [ERROR-INJECTION-yz-AlternateSuccession(y,z).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-yz-AlternateSuccession(y,z).html)
     - [ERROR-INJECTION-ü§-NotCoExistence(ü,§).html](./ErrorInjectionExperiment/ERROR-INJECTION-TASKS-WHITE-NOISE-PLOTS/ERROR-INJECTION-ü§-NotCoExistence(ü,§).html)
   - **ERROR-INJECTION_TASKS-DELETION-PLOTS/**
     - [ERROR-INJECTION-a-Init(a).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-a-Init(a).html)
     - [ERROR-INJECTION-b-End(b).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-b-End(b).html)
     - [ERROR-INJECTION-c-AtMostOne(c).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-c-AtMostOne(c).html)
     - [ERROR-INJECTION-d-Participation(d).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-d-Participation(d).html)
     - [ERROR-INJECTION-e-Response(e,f).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-e-Response(e,f).html)
     - [ERROR-INJECTION-f-Response(e,f).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-f-Response(e,f).html)
     - [ERROR-INJECTION-g-Precedence(g,h).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-g-Precedence(g,h).html)
     - [ERROR-INJECTION-h-Precedence(g,h).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-h-Precedence(g,h).html)
     - [ERROR-INJECTION-i-AlternatePrecedence(i,l).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-i-AlternatePrecedence(i,l).html)
     - [ERROR-INJECTION-j-ChainSuccession(j,k).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-j-ChainSuccession(j,k).html)
     - [ERROR-INJECTION-k-ChainSuccession(j,k).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-k-ChainSuccession(j,k).html)
     - [ERROR-INJECTION-l-AlternatePrecedence(i,l).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-l-AlternatePrecedence(i,l).html)
     - [ERROR-INJECTION-m-AlternateResponse(m,n).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-m-AlternateResponse(m,n).html)
     - [ERROR-INJECTION-n-AlternateResponse(m,n).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-n-AlternateResponse(m,n).html)
     - [ERROR-INJECTION-o-ChainResponse(o,p).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-o-ChainResponse(o,p).html)
     - [ERROR-INJECTION-p-ChainResponse(o,p).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-p-ChainResponse(o,p).html)
     - [ERROR-INJECTION-q-ChainPrecedence(q,r).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-q-ChainPrecedence(q,r).html)
     - [ERROR-INJECTION-r-ChainPrecedence(q,r).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-r-ChainPrecedence(q,r).html)
     - [ERROR-INJECTION-s-RespondedExistence(s,t).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-s-RespondedExistence(s,t).html)
     - [ERROR-INJECTION-t-RespondedExistence(s,t).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-t-RespondedExistence(s,t).html)
     - [ERROR-INJECTION-u-CoExistence(u,v).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-u-CoExistence(u,v).html)
     - [ERROR-INJECTION-v-CoExistence(u,v).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-v-CoExistence(u,v).html)
     - [ERROR-INJECTION-w-Succession(w,x).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-w-Succession(w,x).html)
     - [ERROR-INJECTION-x-Succession(w,x).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-x-Succession(w,x).html)
     - [ERROR-INJECTION-y-AlternateSuccession(y,z).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-y-AlternateSuccession(y,z).html)
     - [ERROR-INJECTION-z-AlternateSuccession(y,z).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-z-AlternateSuccession(y,z).html)
     - [ERROR-INJECTION-§-NotCoExistence(ü,§).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-§-NotCoExistence(ü,§).html)
     - [ERROR-INJECTION-ü-NotCoExistence(ü,§).html](./ErrorInjectionExperiment/ERROR-INJECTION_TASKS-DELETION-PLOTS/ERROR-INJECTION-ü-NotCoExistence(ü,§).html)
 - **JanusExecutable/**
   - [JanusExecutable.zip](./JanusExecutable/JanusExecutable.zip)
 - **NonDeclareRule/**
   - [JanusExecutable.zip](./NonDeclareRule/JanusExecutable.zip)
   - [NON-DECLARE-results.zip](./NonDeclareRule/NON-DECLARE-results.zip)
 - **PerformancesTests/**
   - [BPICs_with_models.7z](./PerformancesTests/BPICs_with_models.7z)
   - [PERFORMANCE-SPACE-SYNTHETIC-model.json](./PerformancesTests/PERFORMANCE-SPACE-SYNTHETIC-model.json)
   - [PERFORMANCE-SPACE-SYNTHETIC-var-MODEL-model.json](./PerformancesTests/PERFORMANCE-SPACE-SYNTHETIC-var-MODEL-model.json)
   - [PERFORMANCE-SPACE-SYNTHETIC-var-MODEL.sh](./PerformancesTests/PERFORMANCE-SPACE-SYNTHETIC-var-MODEL.sh)
   - [PERFORMANCE-SPACE-SYNTHETIC.sh](./PerformancesTests/PERFORMANCE-SPACE-SYNTHETIC.sh)
   - [PERFORMANCE-SYNTHETIC-initial-model.json](./PerformancesTests/PERFORMANCE-SYNTHETIC-initial-model.json)
   - [PERFORMANCE-SYNTHETIC-log[min_1500_max_2000_size_500].txt](./PerformancesTests/PERFORMANCE-SYNTHETIC-log[min_1500_max_2000_size_500].txt)
   - [PERFORMANCE-SYNTHETIC-test-model.json](./PerformancesTests/PERFORMANCE-SYNTHETIC-test-model.json)
   - [PERFORMANCE-TIME-BPIC-TIMES.ods](./PerformancesTests/PERFORMANCE-TIME-BPIC-TIMES.ods)
   - [PERFORMANCE-TIME-BPIC.sh](./PerformancesTests/PERFORMANCE-TIME-BPIC.sh)
   - [PERFORMANCE-TIME-SYNTHETIC-var-MODEL.sh](./PerformancesTests/PERFORMANCE-TIME-SYNTHETIC-var-MODEL.sh)
   - [PERFORMANCE-TIME-SYNTHETIC.sh](./PerformancesTests/PERFORMANCE-TIME-SYNTHETIC.sh)
   - [space-BPIC.ods](./PerformancesTests/space-BPIC.ods)
 - **RankingExperiment/**
   - [GROUND-TRUTH-NEU-NOISE-measures-average-ranking[TOT-nanLogSkip][RESULT].ods](./RankingExperiment/GROUND-TRUTH-NEU-NOISE-measures-average-ranking[TOT-nanLogSkip][RESULT].ods)
   - [GROUND-TRUTH-NEU-NOISE-model.json](./RankingExperiment/GROUND-TRUTH-NEU-NOISE-model.json)
   - [GROUND-TRUTH-NEU-NOISE-results.zip](./RankingExperiment/GROUND-TRUTH-NEU-NOISE-results.zip)
   - [GROUND-TRUTH-NEU-NOISE.sh](./RankingExperiment/GROUND-TRUTH-NEU-NOISE.sh)
   - [GROUND-TRUTH-NEU-SEPSIS-measures-ranking[TOT-nanLogSkip][RESULT].ods](./RankingExperiment/GROUND-TRUTH-NEU-SEPSIS-measures-ranking[TOT-nanLogSkip][RESULT].ods)
   - [GROUND-TRUTH-NEU-SEPSIS-model.json](./RankingExperiment/GROUND-TRUTH-NEU-SEPSIS-model.json)
   - [GROUND-TRUTH-NEU-SEPSIS-results.zip](./RankingExperiment/GROUND-TRUTH-NEU-SEPSIS-results.zip)
   - [GROUND-TRUTH-NEU-SEPSIS.sh](./RankingExperiment/GROUND-TRUTH-NEU-SEPSIS.sh)
   - [GROUND-TRUTH-NEU-measures-average-ranking[TOT-nanLogSkip][RESULT].ods](./RankingExperiment/GROUND-TRUTH-NEU-measures-average-ranking[TOT-nanLogSkip][RESULT].ods)
   - [GROUND-TRUTH-NEU-model.json](./RankingExperiment/GROUND-TRUTH-NEU-model.json)
   - [GROUND-TRUTH-NEU-results.zip](./RankingExperiment/GROUND-TRUTH-NEU-results.zip)
   - [GROUND-TRUTH-NEU.sh](./RankingExperiment/GROUND-TRUTH-NEU.sh)
   - [MEASURES-RANKING[RESULT].ods](./RankingExperiment/MEASURES-RANKING[RESULT].ods)

<!-- filetreestop -->
