---
UID: NA:rxtimer
ms.assetid: 2ab3b1c1-221c-37dd-9599-6b8c422b887b
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# rxtimer.h header



rxtimer.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [RxCancelTimerRequest](nf-rxtimer-rxcanceltimerrequest.md) | RxCancelTimerRequest cancels a recurrent timer request. The request to be canceled is identified by the worker thread routine and associated context. |
| [RxPostOneShotTimerRequest](nf-rxtimer-rxpostoneshottimerrequest.md) | RxPostOneShotTimerRequest initializes a one-shot timer entry. The passed-in pointer to a worker thread routine is called once when the timer expires. |
| [RxPostRecurrentTimerRequest](nf-rxtimer-rxpostrecurrenttimerrequest.md) | RxPostRecurrentTimerRequest initializes a recurrent timer request. The passed in pointer to a worker thread routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine. |