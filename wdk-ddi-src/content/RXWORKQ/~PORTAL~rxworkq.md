# Declarations in the rxworkq header
This header Rxworkq contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RX_DISPATCHER_STATE_ enumeration](ne-rxworkq--rx-dispatcher-state-.md) | TBD |
| [RX_WORK_QUEUE_STATE_ enumeration](ne-rxworkq--rx-work-queue-state-.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxTearDownDispatcher function](nf-rxworkq-rxteardowndispatcher.md) | TBD |
| [RxPostToWorkerThread function](nf-rxworkq-rxposttoworkerthread.md) | RxPostToWorkerThread invokes a routine passed as a parameter in the context of a worker thread. Memory for the WORK_QUEUE_ITEM must be allocated by the caller. |
| [RxInitializeDispatcher function](nf-rxworkq-rxinitializedispatcher.md) | TBD |
| [RxDispatchToWorkerThread function](nf-rxworkq-rxdispatchtoworkerthread.md) | RxDispatchToWorkerThread invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM is allocated by this routine. |
| [RxInitializeMRxDispatcher function](nf-rxworkq-rxinitializemrxdispatcher.md) | TBD |
| [RxSpinDownMRxDispatcher function](nf-rxworkq-rxspindownmrxdispatcher.md) | RxSpinDownMRxDispatcher tears down the dispatcher context for a network mini-redirector. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [RX_WORK_QUEUE_RUNDOWN_CONTEXT_ structure](ns-rxworkq--rx-work-queue-rundown-context-.md) | TBD |
| [RX_WORK_QUEUE_DISPATCHER_ structure](ns-rxworkq--rx-work-queue-dispatcher-.md) | TBD |
| [RX_WORK_DISPATCH_ITEM_ structure](ns-rxworkq--rx-work-dispatch-item-.md) | TBD |
| [RX_WORK_QUEUE_ITEM_ structure](ns-rxworkq--rx-work-queue-item-~r1.md) | TBD |
| [RX_WORK_QUEUE_ structure](ns-rxworkq--rx-work-queue-.md) | TBD |
| [RX_WORK_QUEUE_ITEM_ structure](ns-rxworkq--rx-work-queue-item-.md) | TBD |
| [RX_DISPATCHER_ structure](ns-rxworkq--rx-dispatcher-.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PRX_WORKERTHREAD_ROUTINE callback function](nc-rxworkq-prx-workerthread-routine.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
