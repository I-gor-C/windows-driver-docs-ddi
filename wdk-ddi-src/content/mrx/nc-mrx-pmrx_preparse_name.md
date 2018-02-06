---
UID: NC:mrx.PMRX_PREPARSE_NAME
title: PMRX_PREPARSE_NAME
author: windows-driver-content
description: The MRxPreparseName routine is called by RDBSS to give a network mini-redirector the opportunity to preparse a name.
old-location: ifsk\mrxpreparsename.htm
old-project: ifsk
ms.assetid: b74acc12-8fc2-497f-9f65-8b1a85a03286
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: ifsk.mrxpreparsename, MRxPreparseName routine [Installable File System Drivers], MRxPreparseName, PMRX_PREPARSE_NAME, PMRX_PREPARSE_NAME, mrx/MRxPreparseName, mrxref_4f7f0d54-93a0-4b61-bf62-6e7b1063415c.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	mrx.h
apiname:
-	MRxPreparseName
product: Windows
targetos: Windows
req.typenames: SetDSMCounters_IN, *PSetDSMCounters_IN
---


# PMRX_PREPARSE_NAME callback function
The<i> MRxPreparseName</i> routine is called by <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/the-rdbss-driver-and-library">RDBSS</a> to give a network mini-redirector the opportunity to preparse a name.

## Syntax

```
PMRX_PREPARSE_NAME PmrxPreparseName;

NTSTATUS PmrxPreparseName(
  IN OUT PRX_CONTEXT RxContext,
  IN PUNICODE_STRING Name
)
{...}
```

## Parameters

`RxContext`

A pointer to the RX_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

`Name`

A pointer to a Unicode string that contains the name string.


## Return Value

<i>MRxPreparseName</i> returns STATUS_SUCCESS on success.

## Remarks

<i>MRxPreparseName</i> is called by RDBSS after parsing a name to give a network mini-redirector a final opportunity to preparse the name. 

RDBSS tries to convert the name to its canonical form, removing a dot (".") and two dots (".."), before calling <i>MRxPreparseName</i>. RDBSS will also parse the format used by NTFS streams. 

RDBSS ignores the return value from <i>MRxPreparseName</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | mrx.h (include Mrx.h) |

## See Also

<a href="..\fcb\nf-fcb-rxfinalizesrvcall.md">RxFinalizeSrvCall</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549864">MRxCreateSrvCall</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550663">MRxFinalizeVNetRoot</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550824">MRxSrvCallWinnerNotify</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550653">MRxFinalizeNetRoot</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549869">MRxCreateVNetRoot</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550649">MRxExtractNetRootName</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxPreparseName routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>