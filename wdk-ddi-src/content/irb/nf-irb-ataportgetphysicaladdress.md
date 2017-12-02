---
UID: NF.irb.AtaPortGetPhysicalAddress
title: AtaPortGetPhysicalAddress
author: windows-driver-content
description: The AtaPortGetPhysicalAddress routine converts the virtual address range to the physical address range.
old-location: storage\ataportgetphysicaladdress.htm
old-project: storage
ms.assetid: f6c595f2-a493-453a-a744-7ce6577ae29e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AtaPortGetPhysicalAddress
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
req.alt-api: AtaPortGetPhysicalAddress
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
req.iface: 
---

# AtaPortGetPhysicalAddress function



## -description
<p>The <b>AtaPortGetPhysicalAddress</b> routine converts the virtual address range to the physical address range. </p>


## -syntax

````
IDE_PHYSICAL_ADDRESS AtaPortGetPhysicalAddress(
  _In_      PVOID              ChannelExtension,
  _In_opt_  PIDE_REQUEST_BLOCK Irb,
  _In_opt_  PVOID              VirtualAddress,
  _Out_opt_ ULONG              *Length
);
````


## -parameters
<dl>

### -param ChannelExtension [in]

<dd>
<p>A pointer to the channel extension. </p>
</dd>

### -param Irb [in, optional]

<dd>
<p>A pointer to a structure of type <a href="..\irb\ns-irb--ide-request-block.md">IDE_REQUEST_BLOCK</a> that defines the IDE request block (IRB) for which the address range is converted. </p>
</dd>

### -param VirtualAddress [in, optional]

<dd>
<p>A pointer to the base virtual address to convert. </p>
</dd>

### -param Length [out, optional]

<dd>
<p>Returns the number of mapped bytes starting at the returned physical address. </p>
</dd>
</dl>

## -returns
<p><b>AtaPortGetPhysicalAddress </b>returns the corresponding physical address for the virtual address. If the virtual address cannot be converted, it returns <b>NULL</b>. </p>

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
<a href="..\irb\ns-irb--ide-request-block.md">IDE_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortGetPhysicalAddress routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
