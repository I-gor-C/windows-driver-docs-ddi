---
UID: NS.ndis._NDIS_PROTOCOL_PAUSE_PARAMETERS
title: NDIS_PROTOCOL_PAUSE_PARAMETERS
author: windows-driver-content
description: NDIS passes an NDIS_PROTOCOL_PAUSE_PARAMETERS structure to a protocol driver when it calls the ProtocolNetPnPEvent function to indicate a NetEventPause event.
old-location: netvista\ndis_protocol_pause_parameters.htm
old-project: netvista
ms.assetid: 7754d47f-9e21-44c7-8a6f-141d18623ddf
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_PROTOCOL_PAUSE_PARAMETERS, NDIS_PROTOCOL_PAUSE_PARAMETERS, *PNDIS_PROTOCOL_PAUSE_PARAMETERS
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
req.alt-api: NDIS_PROTOCOL_PAUSE_PARAMETERS
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

# NDIS_PROTOCOL_PAUSE_PARAMETERS structure



## -description
<p>NDIS passes an NDIS_PROTOCOL_PAUSE_PARAMETERS structure to a protocol driver when it calls the 
  <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> function to
  indicate a 
  <b>NetEventPause</b> event.</p>


## -syntax

````
typedef struct _NDIS_PROTOCOL_PAUSE_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  ULONG              PauseReason;
} NDIS_PROTOCOL_PAUSE_PARAMETERS, *PNDIS_PROTOCOL_PAUSE_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_PROTOCOL_PAUSE_PARAMETERS structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_PROTOCOL_PAUSE_PARAMETERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_PROTOCOL_PAUSE_PARAMETERS_REVISION_1.</p>
</dd>

### -field Flags

<dd>
<p>Reserved.</p>
</dd>

### -field PauseReason

<dd>
<div class="alert"><b>Note</b>  This member is deprecated for NDIS 6.40 and later drivers.</div>
<div> </div>
<p>The value will always be NDIS_PAUSE_NDIS_INTERNAL.</p>
</dd>
</dl>

## -remarks
<p>To specify the pause parameters for a binding, NDIS passes a pointer to an
    NDIS_PROTOCOL_PAUSE_PARAMETERS structure to the 
    <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> function when
    NDIS indicates a 
    <b>NetEventPause</b> event.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROTOCOL_PAUSE_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
