---
UID: NI.ks.IOCTL_KS_ENABLE_EVENT
title: IOCTL_KS_ENABLE_EVENT
author: windows-driver-content
description: An application can use IOCTL_KS_ENABLE_EVENT to request notification of a KS event type, or to determine the events supported by a KS object.
old-location: stream\ioctl_ks_enable_event.htm
old-project: stream
ms.assetid: 194a99f4-900f-44d1-bbc3-64953e4dce21
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _KsEdit
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_KS_ENABLE_EVENT
req.alt-loc: ks.h
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
---

# IOCTL_KS_ENABLE_EVENT IOCTL



## -description

An application can use IOCTL_KS_ENABLE_EVENT to request notification of a KS event type, or to determine the events supported by a KS object. The application specifies IOCTL_KS_ENABLE_EVENT in the <b>IoControl</b> parameter of a call to <a href="stream.kssynchronousdevicecontrol">KsSynchronousDeviceControl</a>.



An application can use IOCTL_KS_ENABLE_EVENT to request notification of a KS event type, or to determine the events supported by a KS object. The application specifies IOCTL_KS_ENABLE_EVENT in the <b>IoControl</b> parameter of a call to <a href="stream.kssynchronousdevicecontrol">KsSynchronousDeviceControl</a>.



## -ioctlparameters

### -input-buffer
The application places a pointer to a structure of type <a href="stream.ksevent">KSEVENT</a> in the <b>InBuffer</b> parameter and the size of this structure at <b>InLength</b>. 


### -input-buffer-length
Length of <a href="stream.ksevent">KSEVENT</a>.


### -output-buffer
The application places a pointer to a structure of type <a href="stream.kseventdata">KSEVENTDATA</a> in the <b>OutBuffer</b> parameter and the size of this structure at <b>OutLength</b>. 


### -output-buffer-length
Length of <a href="stream.kseventdata">KSEVENTDATA</a>.


### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
If the request is successful, the Status member is set to STATUS_SUCCESS.


## -remarks
To determine events supported by a KS object, specify <b>NULL</b> and 0 respectively for <b>InBuffer</b> and <b>InLength</b>.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ni-ks-ioctl_ks_disable_event.md">IOCTL_KS_DISABLE_EVENT</a>
</dt>
<dt>
<a href="stream.ksevent_item">KSEVENT_ITEM</a>
</dt>
<dt>
<a href="stream.ksevent_set">KSEVENT_SET</a>
</dt>
<dt>
<a href="stream.ksevent_entry">KSEVENT_ENTRY</a>
</dt>
<dt>
<a href="stream.ksdpc_item">KSDPC_ITEM</a>
</dt>
<dt>
<a href="stream.kseventdata">KSEVENTDATA</a>
</dt>
<dt>
<a href="stream.ksevent">KSEVENT</a>
</dt>
<dt>
<a href="stream.ksdisableevent">KsDisableEvent</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IOCTL_KS_ENABLE_EVENT control code%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

