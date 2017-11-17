---
UID: NS.ntddndis._NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO
title: NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO
author: windows-driver-content
description: The NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO structure contains information about a Hyper-V extensible switch port policy property.
old-location: netvista\ndis_switch_port_property_enum_info.htm
ms.assetid: 537342c3-fbcf-493d-98ce-64ea1a84225b
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO
req.alt-loc: Ntddndis.h
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
ms.keywords: NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO, NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO, *PNDIS_SWITCH_PORT_PROPERTY_ENUM_INFO
req.iface: 
---

# NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO structure



## -description
<p>The <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structure contains information about a Hyper-V extensible switch port policy property.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO {
  NDIS_OBJECT_HEADER             Header;
  ULONG                          Flags;
  NDIS_SWITCH_OBJECT_VERSION     PropertyVersion;
  NDIS_SWITCH_OBJECT_INSTANCE_ID PropertyInstanceId;
  ULONG                          QwordAlignedPropertyBufferLength;
  ULONG                          PropertyBufferLength;
  ULONG                          PropertyBufferOffset;
} NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO, *PNDIS_SWITCH_PORT_PROPERTY_ENUM_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value:  </p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_REVISION_1"></a><a id="ndis_switch_port_property_enum_info_revision_1"></a>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>PropertyVersion</b>

<dd>
<p>An NDIS_SWITCH_OBJECT_VERSION value that identifies the version of the property for the extensible switch port. </p>
</dd>

### -field <b>PropertyInstanceId</b>

<dd>
<p>An NDIS_SWITCH_OBJECT_INSTANCE_ID value that specifies the instance identifier for the extensible switch port property.

</p>
</dd>

### -field <b>QwordAlignedPropertyBufferLength</b>

<dd>
<p>A ULONG value that specifies the aligned size, in bytes, of the property buffer.</p>
</dd>

### -field <b>PropertyBufferLength</b>

<dd>
<p>A ULONG value that specifies the actual size, in bytes, of the property buffer.</p>
<div class="alert"><b>Note</b>  This value must be less than or equal to the value of the <b>QwordAlignedPropertyBufferLength</b> member.</div>
<div> </div>
</dd>

### -field <b>PropertyBufferOffset</b>

<dd>
<p>A ULONG value that specifies the offset, in bytes, to the property buffer that follows the <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structure. The offset is measured from the start of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598238">NDIS_SWITCH_PORT_PROPERTY_PARAMETERS</a> structure up to the beginning of the property buffer.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structure is used in OID method requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598277">OID_SWITCH_PORT_PROPERTY_ENUM</a>. An array of <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structures follow the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598236">NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS</a> structure in the information buffer that is associated with this OID request. The <b>InformationBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure contains a pointer to this information buffer.</p>

<p>Extensible switch extensions can access the next <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> element that follows an <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structure in the array  by using the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598234">NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_NEXT</a> macro.</p>

<p>Extensible switch extensions can access the port property buffer that is specified by an <b>NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO</b> structure  by using the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598235">NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_PROPERTY</a> macro.</p>

<p>For more information about extensible switch policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598234">NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_NEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598235">NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598236">NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598277">OID_SWITCH_PORT_PROPERTY_ENUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
