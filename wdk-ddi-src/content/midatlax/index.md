---
UID : NA:midatlax
ms.assetid : e8c80790-7ec0-3fdc-83c7-699e2f78cdb7
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# midatlax.h header



midatlax.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [RxAssociateContextWithMid](nf-midatlax-rxassociatecontextwithmid.md) | RxAssociateContextWithMid associates the supplied opaque context with an available multiplex ID (MID) from a MID_ATLAS. |
| [RxCreateMidAtlas](nf-midatlax-rxcreatemidatlas.md) | RxCreateMidAtlas allocates a new instance of MID_ATLAS data structure and initializes it. |
| [RxDestroyMidAtlas](nf-midatlax-rxdestroymidatlas.md) | RxDestroyMidAtlas destroys an existing instance of a MID_ATLAS data structure and frees the allocated memory. |
| [RxMapAndDissociateMidFromContext](nf-midatlax-rxmapanddissociatemidfromcontext.md) | RxMapAndDissociateMidFromContext maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure and then disassociates the MID from the context. |
| [RxMapMidToContext](nf-midatlax-rxmapmidtocontext.md) | RxMapMidToContext maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure. |
| [RxReassociateMid](nf-midatlax-rxreassociatemid.md) | RxReassociateMid reassociates a Multiplex ID (MID) with an alternate context. |