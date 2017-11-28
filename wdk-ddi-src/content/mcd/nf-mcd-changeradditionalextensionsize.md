---
UID: NF.mcd.ChangerAdditionalExtensionSize
title: ChangerAdditionalExtensionSize
author: windows-driver-content
description: ChangerAdditionalExtensionSize indicates the number of bytes the changer miniclass driver requires to store device-specific information in the device extension.
old-location: storage\changeradditionalextensionsize.htm
old-project: storage
ms.assetid: d9bcbad5-ce2c-4968-9544-4fb024b1e933
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerAdditionalExtensionSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ChangerAdditionalExtensionSize
req.alt-loc: mcd.h
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

# ChangerAdditionalExtensionSize function



## -description
<p><b>ChangerAdditionalExtensionSize</b> indicates the number of bytes the changer miniclass driver requires to store device-specific information in the device extension.</p>


## -syntax

````
ULONG ChangerAdditionalExtensionSize(void);
````


## -parameters


## -returns
<p><b>ChangerAdditionalExtensionSize</b> returns the size, in bytes, of the additional device extension space required by the changer miniclass driver. </p>

<p><b>ChangerAdditionalExtensionSize</b> returns the size, in bytes, of the additional device extension space required by the changer miniclass driver. </p>

<p><b>ChangerAdditionalExtensionSize</b> returns the size, in bytes, of the additional device extension space required by the changer miniclass driver. </p>

## -remarks
<p>The changer class driver calls <b>ChangerAdditionalExtensionSize</b> to determine the number of bytes the miniclass driver requires in the device extension for a particular changer before creating the device object to represent that changer.</p>

<p>The device-specific information stored by a changer miniclass driver is determined by the driver. It typically includes zero-based offsets that other miniclass driver routines can use to translate between device-specific element addresses and the zero-based element addresses used by the system. It can also include SCSI inquiry data or the non-SCSI equivalent.</p>

<p>The changer class driver calls <b>ChangerAdditionalExtensionSize</b> to determine the number of bytes the miniclass driver requires in the device extension for a particular changer before creating the device object to represent that changer.</p>

<p>The device-specific information stored by a changer miniclass driver is determined by the driver. It typically includes zero-based offsets that other miniclass driver routines can use to translate between device-specific element addresses and the zero-based element addresses used by the system. It can also include SCSI inquiry data or the non-SCSI equivalent.</p>

<p>The changer class driver calls <b>ChangerAdditionalExtensionSize</b> to determine the number of bytes the miniclass driver requires in the device extension for a particular changer before creating the device object to represent that changer.</p>

<p>The device-specific information stored by a changer miniclass driver is determined by the driver. It typically includes zero-based offsets that other miniclass driver routines can use to translate between device-specific element addresses and the zero-based element addresses used by the system. It can also include SCSI inquiry data or the non-SCSI equivalent.</p>

<p>The changer class driver calls <b>ChangerAdditionalExtensionSize</b> to determine the number of bytes the miniclass driver requires in the device extension for a particular changer before creating the device object to represent that changer.</p>

<p>The device-specific information stored by a changer miniclass driver is determined by the driver. It typically includes zero-based offsets that other miniclass driver routines can use to translate between device-specific element addresses and the zero-based element addresses used by the system. It can also include SCSI inquiry data or the non-SCSI equivalent.</p>

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
<dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551431">ChangerInitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ChangerAdditionalExtensionSize function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
