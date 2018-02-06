---
UID: NA:fwpmk
ms.assetid: 8f2f932d-18da-3dec-85cf-ff744e0bedb4
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# fwpmk.h header



fwpmk.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [FwpmBfeStateGet0](nf-fwpmk-fwpmbfestateget0.md) | The FwpmBfeStateGet0 function retrieves the current state of the filter engine.Note  FwpmBfeStateGet0 is a specific version of FwpmBfeStateGet. |
| [FwpmBfeStateSubscribeChanges0](nf-fwpmk-fwpmbfestatesubscribechanges0.md) | The FwpmBfeStateSubscribeChanges0 function registers a callback function that is called whenever there is a change to the state of the filter engine.Note  FwpmBfeStateSubscribeChanges0 is a specific version of FwpmBfeStateSubscribeChanges. |
| [FwpmBfeStateUnsubscribeChanges0](nf-fwpmk-fwpmbfestateunsubscribechanges0.md) | The FwpmBfeStateUnsubscribeChanges0 function deregisters a base filtering engine (BFE) callback function that was previously registered by calling the FwpmBfeStateSubscribeChanges0 function.Note  FwpmBfeStateUnsubscribeChanges0 is a specific version of FwpmBfeStateUnsubscribeChanges. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. |
| [FwpmCalloutAdd0](nf-fwpmk-fwpmcalloutadd0.md) | The FwpmCalloutAdd0 function adds a callout to the filter engine.Note  FwpmCalloutAdd0 is a specific version of FwpmCalloutAdd. |
| [FwpmCalloutDeleteById0](nf-fwpmk-fwpmcalloutdeletebyid0.md) | The FwpmCalloutDeleteById0 function deletes a callout from the filter engine.Note  FwpmCalloutDeleteById0 is a specific version of FwpmCalloutDeleteById. |
| [FwpmCalloutDeleteByKey0](nf-fwpmk-fwpmcalloutdeletebykey0.md) | The FwpmCalloutDeleteByKey0 function deletes a callout from the filter engine.Note  FwpmCalloutDeleteByKey0 is a specific version of FwpmCalloutDeleteByKey. |
| [FwpmEngineClose0](nf-fwpmk-fwpmengineclose0.md) | The FwpmEngineClose0 function closes a previously opened session to the filter engine.Note  FwpmEngineClose0 is a specific version of FwpmEngineClose. |
| [FwpmEngineOpen0](nf-fwpmk-fwpmengineopen0.md) | The FwpmEngineOpen0 function opens a session to the filter engine.Note  FwpmEngineOpen0 is a specific version of FwpmEngineOpen. |