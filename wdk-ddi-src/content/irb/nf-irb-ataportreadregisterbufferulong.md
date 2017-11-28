---
UID: NF.irb.AtaPortReadRegisterBufferUlong
title: AtaPortReadRegisterBufferUlong
author: windows-driver-content
description: The AtaPortReadRegisterBufferUlong routine transfers a specified number of ULONG values from the HBA to a buffer.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportreadregisterbufferulong.htm
old-project: storage
ms.assetid: 50baeaa1-5671-4f6d-83cd-f03cca18b18b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AtaPortReadRegisterBufferUlong
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
req.alt-api: AtaPortReadRegisterBufferUlong
req.alt-loc: ataport.lib,ataport.dll,pciidex.lib,pciidex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ataport.lib; 
Pciidex.lib
req.dll: 
req.irql: 
req.iface: 
---

# AtaPortReadRegisterBufferUlong function



## -description
<p>The <b>AtaPortReadRegisterBufferUlong</b> routine transfers a specified number of ULONG values from the HBA to a buffer.</p>


## -syntax

````
VOID AtaPortReadRegisterBufferUlong(
  _In_ PULONG Register,
  _In_ PULONG Buffer,
  _In_ ULONG  Count
);
````


## -parameters
<dl>

### -param <i>Register</i> [in]

<dd>
<p>Contains the register address where the transfer should begin. This address value must be within the range of mapped I/O space addresses that are obtained by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff550160">AtaPortGetDeviceBase</a>.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to the destination buffer.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of ULONG values to read from the HBA.</p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks


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
<tr>
<th width="30%">
<p>Library</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550160">AtaPortGetDeviceBase</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550188">AtaPortReadRegisterBufferUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550192">AtaPortReadRegisterBufferUshort</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortReadRegisterBufferUlong routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
