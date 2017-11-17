---
UID: NS.hbapiwmi._HBAFC3MgmtInfo
title: HBAFC3MgmtInfo
author: windows-driver-content
description: The HBAFC3MgmtInfo structure is used to report FC3 management information associated with a fibre channel adapter.
old-location: storage\hbafc3mgmtinfo.htm
ms.assetid: 96236605-36b0-48f5-85d6-512160692b5f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBAFC3MgmtInfo
req.alt-loc: hbapiwmi.h
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
ms.keywords: HBAFC3MgmtInfo, HBAFC3MgmtInfo, *PHBAFC3MgmtInfo
req.iface: 
---

# HBAFC3MgmtInfo structure



## -description
<p>The HBAFC3MgmtInfo structure is used to report FC3 management information associated with a fibre channel adapter. </p>


## -syntax

````
typedef struct _HBAFC3MgmtInfo {
  ULONGLONG UniqueAdapterId;
  UCHAR     wwn[8];
  ULONG     unittype;
  ULONG     PortId;
  ULONG     NumberOfAttachedNodes;
  USHORT    IPVersion;
  USHORT    UDPPort;
  UCHAR     IPAddress[16];
  USHORT    reserved;
  USHORT    TopologyDiscoveryFlags;
  ULONG     reserved1;
} HBAFC3MgmtInfo, *PHBAFC3MgmtInfo;
````


## -struct-fields
<dl>

### -field <b>UniqueAdapterId</b>

<dd>
<p>Contains a unique identifier for the adapter. </p>
</dd>

### -field <b>wwn</b>

<dd>
<p>Contains a worldwide name for the adapter, as described in the T11 committee's <i>Fibre Channel HBA API </i>specification. </p>
</dd>

### -field <b>unittype</b>

<dd>
<p>Describes the type of HBA, as described in the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>
</dd>

### -field <b>PortId</b>

<dd>
<p>Contains a value corresponding to the physical port number field of the specific identification data as described in the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>
</dd>

### -field <b>NumberOfAttachedNodes</b>

<dd>
<p>Contains the number of nodes attached to the topology as described in the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>
</dd>

### -field <b>IPVersion</b>

<dd>
<p>Contains the concatenated node management and IP version fields of the specific identification data as described in the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>
</dd>

### -field <b>UDPPort</b>

<dd>
<p>Indicates the value of the UDP/TCP port number field of the specific identification data as described in the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>
</dd>

### -field <b>IPAddress</b>

<dd>
<p>Indicates the value of the IP address field of the specific identification data as described in the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>
</dd>

### -field <b>reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>TopologyDiscoveryFlags</b>

<dd>
<p>Indicates the value of the vendor specific field in word 12 of the specific identification data as described in the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>
</dd>

### -field <b>reserved1</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>FC-3 refers to the common services layer of the fibre channel protocol. It defines a set of services which are common across multiple ports of a node. For an explanation of the common services layer, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>

<p>The WMI tool suite generates a declaration of this structure automatically when it compiles the <b>HBAFC3MgmtInfo</b> WMI Class in <i>hbaapi.mof</i>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553939">GetFC3MgmtInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBAFC3MgmtInfo structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
