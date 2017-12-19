---
UID: NF.srb.ScsiPortConvertPhysicalAddressToUlong~r1
title: ScsiPortConvertPhysicalAddressToUlong macro
author: windows-driver-content
description: The ScsiPortConvertPhysicalAddressToUlong routine truncates a SCSI_PHYSICAL_ADDRESS to a ULONG.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
old-location: storage\scsiportconvertphysicaladdresstoulong.htm
old-project: storage
ms.assetid: 55c258d2-922a-430a-ba6b-b05a078b712d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: ScsiPortConvertPhysicalAddressToUlong
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: srb.h
req.include-header: Miniport.h, Scsi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiPortConvertPhysicalAddressToUlong
req.alt-loc: Scsiport.lib,Scsiport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Scsiport.lib
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# ScsiPortConvertPhysicalAddressToUlong macro



## -description
The <b>ScsiPortConvertPhysicalAddressToUlong</b> routine truncates a SCSI_PHYSICAL_ADDRESS to a ULONG.



## -syntax

````
ULONG ScsiPortConvertPhysicalAddressToUlong(
  _In_ SCSI_PHYSICAL_ADDRESS Address
);
````


## -parameters

### -param Address [in]

Specifies a value of type SCSI_PHYSICAL_ADDRESS.


## -remarks


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
Header

</th>
<td width="70%">
<dl>
<dt>Srb.h (include Miniport.h or Scsi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Scsiport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.access_range">ACCESS_RANGE</a>
</dt>
<dt>
<a href="storage.scsiportgetdevicebase">ScsiPortGetDeviceBase</a>
</dt>
<dt>
<a href="storage.scsiportgetphysicaladdress">ScsiPortGetPhysicalAddress</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiPortConvertPhysicalAddressToUlong routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

