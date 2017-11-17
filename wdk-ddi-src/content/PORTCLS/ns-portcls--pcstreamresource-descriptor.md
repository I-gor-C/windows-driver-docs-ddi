---
UID: NS.portcls._PCSTREAMRESOURCE_DESCRIPTOR
title: PCSTREAMRESOURCE_DESCRIPTOR
author: windows-driver-content
description: PCSTREAMRESOURCE_DESCRIPTOR defines the stream resource. Use PCSTREAMRESOURCE_DESCRIPTOR_INIT to correctly initialize this structure.
old-location: audio\pcstreamresource_descriptor.htm
ms.assetid: 978D06FC-B5CC-409C-BE5D-CA4B53005D8C
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCSTREAMRESOURCE_DESCRIPTOR
req.alt-loc: Portcls.h
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
ms.keywords: PCSTREAMRESOURCE_DESCRIPTOR, PCSTREAMRESOURCE_DESCRIPTOR, *PPCSTREAMRESOURCE_DESCRIPTOR
req.iface: 
---

# PCSTREAMRESOURCE_DESCRIPTOR structure



## -description
<p>PCSTREAMRESOURCE_DESCRIPTOR defines the stream resource. Use PCSTREAMRESOURCE_DESCRIPTOR_INIT to correctly initialize this structure. </p>


## -syntax

````
typedef struct _PCSTREAMRESOURCE_DESCRIPTOR {
  ULONG                Size;
  ULONG                Flags;
  PDEVICE_OBJECT       Pdo;
  PcStreamResourceType Type;
  union {
    struc {
      ULONG Version;
      PVOID Generic;
    }     Interrupt;
    PETHREAD Thread;
    PVOID     ResourceSet;
  } Resource;
} PCSTREAMRESOURCE_DESCRIPTOR, *PPCSTREAMRESOURCE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p> This field is init to the size of the struct.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for future use. Set to zero. 
</p>
</dd>

### -field <b>Pdo</b>

<dd>
<p>The physical device object of the stack that created this resource. </p>
</dd>

### -field <b>Type</b>

<dd>
<p>The union of the different stream resource types.</p>
</dd>

### -field <b>Resource</b>

<dd>
<dl>

### -field <b>Thread</b>

<dd>
<p>Thread.</p>
</dd>

### -field <b> ResourceSet</b>

<dd>
<p>Reserved for future use, set to NULL. Only device-scoped resources are supported at this time.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>Stream resources are any resources used by the audio driver to process audio streams or ensure audio data flow. Two type of stream resources are supported: interrupts and driver-owned threads. Audio drivers should register a resource after creating the resource, and unregister the resource before deleted it. 
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt298190">PcStreamResourceType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCSTREAMRESOURCE_DESCRIPTOR structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
