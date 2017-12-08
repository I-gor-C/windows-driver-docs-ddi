---
UID: NF.video.VideoPortQueueDpc
title: VideoPortQueueDpc function
author: windows-driver-content
description: The VideoPortQueueDpc function allows a miniport driver to queue a DPC.
old-location: display\videoportqueuedpc.htm
old-project: display
ms.assetid: 9715ff37-397b-4102-a363-443b8076f881
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: VideoPortQueueDpc
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortQueueDpc
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: >= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# VideoPortQueueDpc function



## -description
The <b>VideoPortQueueDpc</b> function allows a miniport driver to queue a DPC.


## -syntax

````
BOOLEAN VideoPortQueueDpc(
  _In_ PVOID                 HwDeviceExtension,
  _In_ PMINIPORT_DPC_ROUTINE CallbackRoutine,
  _In_ PVOID                 Context
);
````


## -parameters

### -param HwDeviceExtension [in]

Pointer to the miniport driver's device extension.

### -param CallbackRoutine [in]

Pointer to the miniport driver's <a href="..\video\nc-video-pminiport_dpc_routine.md">HwVidDpcRoutine</a> to be called when the DPC is scheduled. The callback routine must be nonpaged.

### -param Context [in]

Pointer to the miniport driver-supplied context that will be passed to <i>CallbackRoutine</i>.

## -returns
<b>VideoPortQueueDpc</b> returns <b>TRUE</b> if the DPC is successfully queued, and <b>FALSE</b> otherwise.

## -remarks
The deferred procedure is run when the IRQL on the current processor drops below DISPATCH_LEVEL. Callers of <b>VideoPortQueueDpc</b> must be running at IRQL &gt;= DISPATCH_LEVEL.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows 2000 and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&gt;= DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nc-video-pminiport_dpc_routine.md">HwVidDpcRoutine</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortQueueDpc function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
