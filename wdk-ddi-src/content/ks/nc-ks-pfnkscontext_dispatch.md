---
UID: NC:ks.PFNKSCONTEXT_DISPATCH
title: PFNKSCONTEXT_DISPATCH
author: windows-driver-content
description: A streaming minidriver's KStrContextDispatch routine is called to process IRP_MJ_POWER IRPs.
old-location: stream\kstrcontextdispatch.htm
old-project: stream
ms.assetid: be96eb59-6128-41bd-ad31-38f0d1a4e656
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KStrContextDispatch, KStrContextDispatch routine [Streaming Media Devices], PFNKSCONTEXT_DISPATCH, ks/KStrContextDispatch, ksfunc_b607dd80-6da6-4364-9452-4c2e53c54343.xml, stream.kstrcontextdispatch
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ks.h
api_name:
-	KStrContextDispatch
product:
- Windows
targetos: Windows
req.typenames: SOUNDDETECTOR_PATTERNHEADER
---


# PFNKSCONTEXT_DISPATCH callback function
A streaming minidriver's <i>KStrContextDispatch</i> routine is called to process IRP_MJ_POWER IRPs.

## Syntax

```
PFNKSCONTEXT_DISPATCH PfnkscontextDispatch;

NTSTATUS PfnkscontextDispatch(
  PVOID Context,
  PIRP Irp
)
{...}
```

## Parameters

`Context`

Specifies the user-supplied memory context to be passed as the <i>PowerContext</i> argument to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566843">KsSetPowerDispatch</a> function.

`Irp`

Specifies the power IRP to be processed.


## Return Value

Returns STATUS_SUCCESS.

## Remarks

<i>KStrContextDispatch</i> must not complete the power IRP that is passed in the <i>Irp</i> parameter.

To manipulate the list entry only, <i>KStrContextDispatch</i> can call<b> KsSetPowerDispatch</b> while processing the power IRP. Manipulating other list entries can cause enumeration errors.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566843">KsSetPowerDispatch</a>