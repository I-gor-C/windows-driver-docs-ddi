# Declarations in the rxtimer header
This header Rxtimer contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxPostOneShotTimerRequest function](nf-rxtimer-rxpostoneshottimerrequest.md) | RxPostOneShotTimerRequest initializes a one-shot timer entry. The passed-in pointer to a worker thread routine is called once when the timer expires. |
| [RxTearDownRxTimer function](nf-rxtimer-rxteardownrxtimer.md) | TBD |
| [RxPostRecurrentTimerRequest function](nf-rxtimer-rxpostrecurrenttimerrequest.md) | RxPostRecurrentTimerRequest initializes a recurrent timer request. The passed in pointer to a worker thread routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine. |
| [RxCancelTimerRequest function](nf-rxtimer-rxcanceltimerrequest.md) | RxCancelTimerRequest cancels a recurrent timer request. The request to be canceled is identified by the worker thread routine and associated context. |
| [RxInitializeRxTimer function](nf-rxtimer-rxinitializerxtimer.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [RX_WORK_ITEM_ structure](ns-rxtimer--rx-work-item-.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
