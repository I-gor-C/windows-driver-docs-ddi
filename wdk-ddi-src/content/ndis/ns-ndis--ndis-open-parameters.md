---
UID: NS.ndis._NDIS_OPEN_PARAMETERS
title: NDIS_OPEN_PARAMETERS
author: windows-driver-content
description: The NDIS_OPEN_PARAMETERS structure defines the open parameters when a protocol driver calls the NdisOpenAdapterEx function.
old-location: netvista\ndis_open_parameters.htm
old-project: netvista
ms.assetid: bb61026c-311b-41d1-9fcb-3ac44df2025e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_OPEN_PARAMETERS, NDIS_OPEN_PARAMETERS, *PNDIS_OPEN_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_OPEN_PARAMETERS
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_OPEN_PARAMETERS structure



## -description
<p>The NDIS_OPEN_PARAMETERS structure defines the open parameters when a protocol driver calls the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function.</p>


## -syntax

````
typedef struct _NDIS_OPEN_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  PNDIS_STRING       AdapterName;
  PNDIS_MEDIUM       MediumArray;
  UINT               MediumArraySize;
  PUINT              SelectedMediumIndex;
  PNET_FRAME_TYPE    FrameTypeArray;
  UINT               FrameTypeArraySize;
} NDIS_OPEN_PARAMETERS, *PNDIS_OPEN_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_OPEN_PARAMETERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_OPEN_PARAMETERS, the 
     <b>Revision</b> member to NDIS_OPEN_PARAMETERS_REVISION_1, and the 
     <b>Size</b> member to the NDIS_SIZEOF_OPEN_PARAMETERS_REVISION_1.</p>
</dd>

### -field <b>AdapterName</b>

<dd>
<p>A Unicode string that contains the name of the miniport adapter that NDIS passed to 
     <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> in the 
     <b>AdapterName</b> member of the 
     <i>BindParameters</i> parameter. This name can identify a physical adapter (that is, a NIC) or a virtual
     adapter that is associated with an intermediate driver.</p>
</dd>

### -field <b>MediumArray</b>

<dd>
<p>A pointer to an array of 
     <b>NdisMedium<i>Xxx</i></b> values that lists the types of media the caller can support. This list is a subset of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565910">NDIS_MEDIUM</a> types.</p>
</dd>

### -field <b>MediumArraySize</b>

<dd>
<p>The number of elements in the 
     <b>MediumArray</b> member.</p>
</dd>

### -field <b>SelectedMediumIndex</b>

<dd>
<p>A pointer to an driver-provided UINT variable that contains an index into the 
     <b>MediumArray</b> array. NDIS writes this index which identifies the media type that the underlying
     driver uses.</p>
</dd>

### -field <b>FrameTypeArray</b>

<dd>
<p>A pointer to an array of NET_FRAME_TYPE values, specifying the frame types that you want the
     protocol driver to receive. The frame type is a USHORT value that follows the destination and source MAC
     address in Ethernet frames. In the presence of VLAN tags, this value follows the destination, source MAC
     address, and VLAN tag. NET_FRAME_TYPE is defined as follows:
     </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef USHORT  NET_FRAME_TYPE;
typedef NET_FRAME_TYPE *PNET_FRAME_TYPE;</pre>
</td>
</tr>
</table></span></div>
<div class="alert"><b>Note</b>  NDIS uses the frame type values that the protocol driver provides in this array as
     a hint to optimize the receive indications that NDIS sends to the protocol driver. NDIS does not
     guarantee that a protocol driver will receive only packets with frame types that match the types in the
     array.</div>
<div> </div>
</dd>

### -field <b>FrameTypeArraySize</b>

<dd>
<p>The number of elements in the 
     <b>FrameTypeArray</b> member. This number must be equal to or less than
     NDIS_MAX_FRAME_TYPES_PER_OPEN.</p>
</dd>
</dl>

## -remarks
<p>A protocol driver passes an NDIS_OPEN_PARAMETERS structure when it calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function to open a
    miniport adapter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565910">NDIS_MEDIUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OPEN_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
