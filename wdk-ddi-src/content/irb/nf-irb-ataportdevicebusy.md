---
UID: NF.irb.AtaPortDeviceBusy
title: AtaPortDeviceBusy
author: windows-driver-content
description: The AtaPortDeviceBusy routine informs the port driver that the indicated device is busy.
old-location: storage\ataportdevicebusy.htm
old-project: storage
ms.assetid: 919f30b1-025d-4526-a1f6-2d14c482e474
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AtaPortDeviceBusy
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortDeviceBusy
req.alt-loc: irb.h
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
req.iface: 
---

# AtaPortDeviceBusy function



## -description
<p>The <b>AtaPortDeviceBusy</b> routine informs the port driver that the indicated device is busy. </p>


## -syntax

````
VOID __inline AtaPortDeviceBusy(
  _In_ PVOID ChannelExtension,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ ULONG BusyTimeout
);
````


## -parameters
<dl>

### -param ChannelExtension [in]

<dd>
<p>A pointer to the channel extension.</p>
</dd>

### -param TargetId [in]

<dd>
<p>Specifies the target identifier of the device.</p>
</dd>

### -param Lun [in]

<dd>
<p>Specifies the logical unit number (LUN) of the device.</p>
</dd>

### -param BusyTimeout [in]

<dd>
<p>Specifies the time, in seconds, for which the device is presumed to be busy.</p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>When the port driver receives this call, it pauses the request queue for the indicated device for the time that is indicated by <i>BusyTimeout</i>. The caller can pause the channel request queue instead of the request queue for an individual device by assigning the wildcard value of IDE_UNTAGGED to parameters <i>TargetId</i> and <i>Lun</i>. </p>

<p>The port driver automatically resumes paused queues after the time-out interval expires.</p>

<p>The miniport driver must not call <b>AtaPortDeviceBusy</b> from its <a href="storage.idehwinterrupt">IdeHwInterrupt</a> routine.</p>

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
<dt>Irb.h (include Ata.h or Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.idehwinterrupt">IdeHwInterrupt</a>
</dt>
<dt>
<a href="..\irb\nf-irb-ataportdeviceready.md">AtaPortDeviceReady</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortDeviceBusy routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
