---
UID: NF.irb.AtaPortConvertPhysicalAddressToUlong
title: AtaPortConvertPhysicalAddressToUlong function
author: windows-driver-content
description: The AtaPortConvertPhysicalAddressToUlong routine truncates an address of type IDE_PHYSICAL_ADDRESS to a ULONG.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportconvertphysicaladdresstoulong.htm
old-project: storage
ms.assetid: cd63cb65-701e-46e2-ba32-971f91f9eb29
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: AtaPortConvertPhysicalAddressToUlong
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
req.alt-api: AtaPortConvertPhysicalAddressToUlong
req.alt-loc: ataport.lib,ataport.dll,pciidex.lib,pciidex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ataport.lib; Pciidex.lib
req.dll: 
req.irql: 
---

# AtaPortConvertPhysicalAddressToUlong function



## -description
The <b>AtaPortConvertPhysicalAddressToUlong</b> routine truncates an address of type IDE_PHYSICAL_ADDRESS to a ULONG.



## -syntax

````
ULONG AtaPortConvertPhysicalAddressToUlong(
  _In_ IDE_PHYSICAL_ADDRESS Address
);
````


## -parameters

### -param Address [in]

Specifies a value of type IDE_PHYSICAL_ADDRESS.


## -returns
<b>AtaPortConvertPhysicalAddressToUlong</b> returns the lower order part of the given IDE_PHYSICAL_ADDRESS value. 


## -remarks
A miniport driver must not use this routine to truncate a 64-bit physical address. 


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
<dt>Irb.h (include Ata.h or Irb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ataport.lib; </dt>
<dt>Pciidex.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.ataportconvertulongtophysicaladdress">AtaPortConvertUlongToPhysicalAddress</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortConvertPhysicalAddressToUlong routine%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

