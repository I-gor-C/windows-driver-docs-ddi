---
UID: NS.ks._KSMAPPING~r1
title: KSMAPPING
author: windows-driver-content
description: The KSMAPPING structure is used to describe a single contiguous chunk of physical memory for use in scatter/gather DMA operations.
old-location: stream\ksmapping.htm
old-project: stream
ms.assetid: 9a5149dc-5506-4100-80fc-7cd17585d2af
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSMAPPING,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSMAPPING
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
req.iface: 
---

# KSMAPPING structure



## -description
<p>The KSMAPPING structure is used to describe a single contiguous chunk of physical memory for use in scatter/gather DMA operations. </p>


## -syntax

````
typedef struct _KSMAPPING {
  PHYSICAL_ADDRESS PhysicalAddress;
  ULONG            ByteCount;
  ULONG            Alignment;
} KSMAPPING, *PKSMAPPING;
````


## -struct-fields
<dl>

### -field <b>PhysicalAddress</b>

<dd>
<p>This member contains the physical address of this piece of the data frame.</p>
</dd>

### -field <b>ByteCount</b>

<dd>
<p>This member contains the number of bytes of contiguous physical memory in this individual mapping.</p>
</dd>

### -field <b>Alignment</b>

<dd>
<p>This member specifies the memory alignment in bytes for this buffer.</p>
</dd>
</dl>

## -remarks
<p>In order for minidrivers to use this structure within the stream pointer offsets, the pin for which this is referring must specify scatter/gather DMA mapping generation through KSPIN_FLAG_GENERATE_MAPPINGS and the client must register its DMA adapter object with AVStream using <b>KsDeviceRegisterAdapterObject</b>. See <a href="NULL">AVStream DMA Services</a>. The KSPIN_FLAG_GENERATE_MAPPINGS flag is defined on the <a href="..\ks\ns-ks--kspin-descriptor-ex.md">KSPIN_DESCRIPTOR_EX</a> reference page.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="..\ks\ns-ks--ksstream-pointer-offset.md">KSSTREAM_POINTER_OFFSET</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksdeviceregisteradapterobject.md">KsDeviceRegisterAdapterObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSMAPPING structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
