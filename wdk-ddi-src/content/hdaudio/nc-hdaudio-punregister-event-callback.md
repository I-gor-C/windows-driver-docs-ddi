---
UID: NC.hdaudio.PUNREGISTER_EVENT_CALLBACK
title: PUNREGISTER_EVENT_CALLBACK
author: windows-driver-content
description: The UnregisterEventCallback routine deletes the registration of an event callback that was previously registered by a call to RegisterEventCallback.The function pointer type for an UnregisterEventCallback routine is defined as:
old-location: audio\unregistereventcallback.htm
old-project: audio
ms.assetid: 698017a0-13d5-4ed5-a1ce-1a50a62135e0
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: SM_SetRNIDMgmtInfo_OUT, SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: hdaudio.h
req.include-header: Hdaudio.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UnregisterEventCallback
req.alt-loc: hdaudio.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PUNREGISTER_EVENT_CALLBACK callback



## -description
<p>The <i>UnregisterEventCallback</i> routine deletes the registration of an event callback that was previously registered by a call to <a href="..\hdaudio\nc-hdaudio-pregister-event-callback.md">RegisterEventCallback</a>.</p>
<p>The function pointer type for an <i>UnregisterEventCallback</i> routine is defined as:</p>


## -prototype

````
PUNREGISTER_EVENT_CALLBACK UnregisterEventCallback;

NTSTATUS UnregisterEventCallback(
  _In_ PVOID context,
  _In_ UCHAR tag
)
{ ... }
````


## -parameters
<dl>

### -param <i>context</i> [in]

<dd>
<p>Specifies the context value from the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536413">HDAUDIO_BUS_INTERFACE</a><u>, </u><a href="https://msdn.microsoft.com/library/windows/hardware/ff536418">HDAUDIO_BUS_INTERFACE_V2</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a> structure.</p>
</dd>

### -param <i>tag</i> [in]

<dd>
<p>Specifies the tag value that was associated with the callback by the preceding call to <a href="..\hdaudio\nc-hdaudio-pregister-event-callback.md">RegisterEventCallback</a>.</p>
</dd>
</dl>

## -returns
<p><i>UnregisterEventCallback</i> returns STATUS_SUCCESS if the call succeeds in changing the DMA engines' states. Otherwise, the routine returns an appropriate error code. The following table shows a possible return status code.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that the specified tag is not valid.</p>

<p> </p>

## -remarks
<p>Before calling this routine, the function driver is responsible for programming the codec or codecs to remove the association of the callback with the specified tag.</p>

<p>Before calling this routine, the function driver is responsible for programming the codec or codecs to remove the association of the callback with the specified tag.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hdaudio.h (include Hdaudio.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536413">HDAUDIO_BUS_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536418">HDAUDIO_BUS_INTERFACE_V2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pregister-event-callback.md">RegisterEventCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PUNREGISTER_EVENT_CALLBACK callback function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
