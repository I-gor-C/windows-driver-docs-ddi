---
UID: NS.ndis._NDIS_MINIPORT_CO_CHARACTERISTICS
title: NDIS_MINIPORT_CO_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_MINIPORT_CO_CHARACTERISTICS structure specifies the CoNDIS entry points for a CoNDIS miniport driver.
old-location: netvista\ndis_miniport_co_characteristics.htm
ms.assetid: 9348c338-9fb4-4eee-a50f-f709748da56b
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_MINIPORT_CO_CHARACTERISTICS
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
ms.keywords: NDIS_MINIPORT_CO_CHARACTERISTICS, NDIS_MINIPORT_CO_CHARACTERISTICS, *PNDIS_MINIPORT_CO_CHARACTERISTICS
req.iface: 
---

# NDIS_MINIPORT_CO_CHARACTERISTICS structure



## -description
<p>The NDIS_MINIPORT_CO_CHARACTERISTICS structure specifies the CoNDIS entry points for a CoNDIS
  miniport driver.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_CO_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                 Header;
  ULONG                              Flags;
  W_CO_CREATE_VC_HANDLER             CoCreateVcHandler;
  W_CO_DELETE_VC_HANDLER             CoDeleteVcHandler;
  W_CO_ACTIVATE_VC_HANDLER           CoActivateVcHandler;
  W_CO_DEACTIVATE_VC_HANDLER         CoDeactivateVcHandler;
  W_CO_SEND_NET_BUFFER_LISTS_HANDLER CoSendNetBufferListsHandler;
  W_CO_OID_REQUEST_HANDLER           CoOidRequestHandler;
} NDIS_MINIPORT_CO_CHARACTERISTICS, *PNDIS_MINIPORT_CO_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     miniport driver CoNDIS characteristics structure (NDIS_MINIPORT_CO_CHARACTERISTICS). The driver sets the
     
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_CO_MINIPORT_CHARACTERISTICS, the 
     <b>Revision</b> member to NDIS_MINIPORT_CO_CHARACTERISTICS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_MINIPORT_CO_CHARACTERISTICS_REVISION_1.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>CoCreateVcHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/99eaba29-ce17-4e79-878e-5fdf7411e56c">MiniportCoCreateVc</a> function. If
     this entry point is for an integrated miniport call manager (MCM) driver, this member should be <b>NULL</b>,
     because NDIS calls such a driver's 
     <a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a> function
     instead. For more information about 
     <i>ProtocolCoCreateVc</i> in an MCM, see 
     <a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
     NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>.</p>
</dd>

### -field <b>CoDeleteVcHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/ed9b6ad1-059b-47d9-b1f7-10d498c5d2d4">MiniportCoDeleteVc</a> function. If
     this entry point is for an integrated miniport call manager (MCM) driver, this member should be <b>NULL</b>,
     because NDIS calls such a driver's 
     <a href="https://msdn.microsoft.com/d761270f-bf77-441e-834c-9ac7fb3d350f">ProtocolCoDeleteVc</a> function
     instead. For more information about 
     <i>ProtocolCoDeleteVc</i> in an MCM, see 
     <a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
     NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>.</p>
</dd>

### -field <b>CoActivateVcHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/243a1236-4b8a-4f00-9f14-3142fa81c362">
     MiniportCoActivateVc</a> function.</p>
</dd>

### -field <b>CoDeactivateVcHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/8c17cec8-d161-47cf-b886-bb8b8d957656">
     MiniportCoDeactivateVc</a> function.</p>
</dd>

### -field <b>CoSendNetBufferListsHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/4a717842-6d71-488e-a56a-57c6e6e0c5d7">
     MiniportCoSendNetBufferLists</a> function.</p>
</dd>

### -field <b>CoOidRequestHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="https://msdn.microsoft.com/903bcdc5-9d42-4067-a054-057edc95ccf7">
     MiniportCoOidRequest</a> function.</p>
</dd>
</dl>

## -remarks
<p>To specify entry points for CoNDIS, a miniport driver initializes an NDIS_MINIPORT_CO_CHARACTERISTICS
    structure and passes it to the 
    <a href="https://msdn.microsoft.com/97649f4f-942a-47fc-a541-6f160c8b4eb4">
    NdisSetOptionalHandlers</a> function.</p>

<p>The miniport driver calls 
    <b>NdisSetOptionalHandlers</b> from the 
    <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function.</p>

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
<a href="https://msdn.microsoft.com/243a1236-4b8a-4f00-9f14-3142fa81c362">MiniportCoActivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/99eaba29-ce17-4e79-878e-5fdf7411e56c">MiniportCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8c17cec8-d161-47cf-b886-bb8b8d957656">MiniportCoDeactivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ed9b6ad1-059b-47d9-b1f7-10d498c5d2d4">MiniportCoDeleteVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/903bcdc5-9d42-4067-a054-057edc95ccf7">MiniportCoOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4a717842-6d71-488e-a56a-57c6e6e0c5d7">
   MiniportCoSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
   NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d761270f-bf77-441e-834c-9ac7fb3d350f">ProtocolCoDeleteVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_CO_CHARACTERISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
