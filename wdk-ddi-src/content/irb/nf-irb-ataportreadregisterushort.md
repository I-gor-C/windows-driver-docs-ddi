---
UID: NF.irb.AtaPortReadRegisterUshort
title: AtaPortReadRegisterUshort function
author: windows-driver-content
description: The AtaPortReadRegisterUshort routine reads a USHORT value from the HBA.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportreadregisterushort.htm
old-project: storage
ms.assetid: a0a9792c-a2a1-4079-9e1c-c41c5b872fa0
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: AtaPortReadRegisterUshort
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
req.alt-api: AtaPortReadRegisterUshort
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

# AtaPortReadRegisterUshort function



## -description
The <b>AtaPortReadRegisterUshort</b> routine reads a USHORT value from the HBA.



## -syntax

````
USHORT AtaPortReadRegisterUshort(
  _In_ PUSHORT Register
);
````


## -parameters

### -param Register [in]

A pointer to the register to be read. The address value that is assigned to this parameter must be within the range of mapped I/O space addresses that are obtained by a call to <a href="storage.ataportgetdevicebase">AtaPortGetDeviceBase</a>.


## -returns
<b>AtaPortReadRegisterUshort</b> returns a USHORT value from the HBA's register. 


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
<a href="storage.ataportgetdevicebase">AtaPortGetDeviceBase</a>
</dt>
<dt>
<a href="storage.ataportreadregisteruchar">AtaPortReadRegisterUchar</a>
</dt>
<dt>
<a href="storage.ataportreadregisterulong">AtaPortReadRegisterUlong</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortReadRegisterUshort routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

