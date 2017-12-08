---
UID: NS.windot11.DOT11_PHY_ID_LIST
title: DOT11_PHY_ID_LIST
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_phy_id_list.htm
old-project: netvista
ms.assetid: f5b2da7f-69b2-4c3d-85dc-2f616c282c5d
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_PHY_ID_LIST, DOT11_PHY_ID_LIST, *PDOT11_PHY_ID_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_PHY_ID_LIST
req.alt-loc: windot11.h
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
req.product: Windows 10 or later.
---

# DOT11_PHY_ID_LIST structure



## -description

## -syntax

````
typedef struct DOT11_PHY_ID_LIST {
  NDIS_OBJECT_HEADER Header;
  ULONG              uNumOfEntries;
  ULONG              uTotalNumOfEntries;
  ULONG              dot11PhyId[1];
} DOT11_PHY_ID_LIST, *PDOT11_PHY_ID_LIST;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the DOT11_PHY_ID_LIST structure. This member is formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field Type

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field Revision

<dd>
<p>This member must be set to DOT11_PHY_ID_LIST_REVISION_1.</p>
</dd>

### -field Size

<dd>
<p>This member must be set to 
       sizeof(DOT11_PHY_ID_LIST).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field uNumOfEntries

<dd>
<p>The number of entries in the 
     <b>dot11PhyId</b> array.</p>
</dd>

### -field uTotalNumOfEntries

<dd>
<p>The maximum number of entries that the 
     <b>dot11PhyId</b> array can contain.</p>
</dd>

### -field dot11PhyId

<dd>
<p>The list of PHY identifiers (IDs).</p>
</dd>
</dl>

## -remarks
<p>A PHY ID in the 
    <b>dot11PhyId</b> array must be one of the following:</p>

<p>An index into the table of supported PHYs that are defined by the Native 802.11 Operational 
      <b>msDot11SupportedPhyTypes</b> management information base (MIB) object. For more information about PHY
      IDs and the 
      <b>msDot11SupportedPhyTypes</b> MIB object, see 
      <a href="netvista.oid_dot11_supported_phy_types">
      OID_DOT11_SUPPORTED_PHY_TYPES</a>.</p>

<p>A PHY ID with the value of DOT11_PHY_ID_ANY. This PHY ID is called a 
      <i>wildcard PHY ID</i> and is used to specify any supported PHY on the 802.11 station. If the wildcard
      PHY ID is used, it must be the only entry in the 
      <b>dot11PhyId</b> array.</p>

<p>A miniport driver returns the DOT11_PHY_ID_LIST structure when queried by either 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569102">OID_DOT11_ACTIVE_PHY_LIST</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569144">OID_DOT11_DESIRED_PHY_LIST</a>.</p>

<p>When these OIDs are queried, the miniport driver must verify that the 
    <b>InformationBuffer</b> member of the 
    <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function's
    <i>OidRequest</i> parameter is large enough to return the entire DOT11_PHY_ID_LIST structure, including
    all entries in the 
    <b>dot11PhyId</b> array. The value of the 
    <b>InformationBufferLength</b> member of the 
    <i>OidRequest</i> parameter determines what the miniport driver must do, as the following list shows:</p>

<p>If the value of the 
      <b>InformationBufferLength</b> member is less than the length, in bytes, of the entire DOT11_PHY_ID_LIST
      structure, the miniport driver must do the following:</p>

<p>Set the 
        <b>uNumOfEntries</b> member to zero.</p>

<p>Set the 
        <b>uTotalNumOfEntries</b> member to the number of entries in the 
        <b>dot11PhyId</b> array.</p>

<p>For the 
        <i>OidRequest</i> parameter, set the 
        <b>BytesWritten</b> member to zero and the 
        <b>BytesNeeded</b> member to the length, in bytes, of the entire DOT11_PHY_ID_LIST structure.</p>

<p>Fail the query request by returning NDIS_STATUS_BUFFER_OVERFLOW from its 
        <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function.</p>

<p>If the value of the 
      <b>InformationBufferLength</b> member is greater than or equal to the length, in bytes, of the entire
      DOT11_PHY_ID_LIST structure, the miniport driver must do the following to complete a successful query
      request:</p>

<p>For the DOT11_PHY_ID_LIST structure, set the 
        <b>uNumOfEntries</b> and 
        <b>uTotalNumOfEntries</b> members to the total number of entries in the 
        <b>dot11PhyId</b> array.</p>

<p>For the 
        <i>OidRequest</i> parameter, set the 
        <b>BytesNeeded</b> member to zero and the 
        <b>BytesWritten</b> member to the length, in bytes, of the entire DOT11_PHY_ID_LIST structure. The
        miniport driver must also copy the entire DOT11_PHY_ID_LIST structure to the 
        <b>InformationBuffer</b> member.</p>

<p>Return NDIS_STATUS_SUCCESS from its 
        <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569102">OID_DOT11_ACTIVE_PHY_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569144">OID_DOT11_DESIRED_PHY_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_PHY_ID_LIST structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
