---
UID: NS.iscsimgt._ISCSI_ConnectionStaticInfo
title: ISCSI_ConnectionStaticInfo
author: windows-driver-content
description: The ISCSI_ConnectionStaticInfo structure contains information about the characteristics of an established connection.
old-location: storage\iscsi_connectionstaticinfo.htm
old-project: storage
ms.assetid: 14d4464e-d4e8-446c-8822-0b16c984313c
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ISCSI_ConnectionStaticInfo, ISCSI_ConnectionStaticInfo, *PISCSI_ConnectionStaticInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsimgt.h
req.include-header: Iscsimgt.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_ConnectionStaticInfo
req.alt-loc: iscsimgt.h
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

# ISCSI_ConnectionStaticInfo structure



## -description
<p>The ISCSI_ConnectionStaticInfo structure contains information about the characteristics of an established connection.</p>


## -syntax

````
typedef struct _ISCSI_ConnectionStaticInfo {
  ULONGLONG        UniqueConnectionId;
  USHORT           CID;
  UCHAR            State;
  UCHAR            Protocol;
  UCHAR            HeaderIntegrity;
  UCHAR            DataIntegrity;
  USHORT           Reserved;
  ULONG            MaxRecvDataSegmentLength;
  ULONG            AuthType;
  ISCSI_IP_Address LocalAddr;
  ULONG            LocalPort;
  ISCSI_IP_Address RemoteAddr;
  ULONG            RemotePort;
  ULONGLONG        EstimatedThroughput;
  ULONG            MaxDatagramSize;
} ISCSI_ConnectionStaticInfo, *PISCSI_ConnectionStaticInfo;
````


## -struct-fields
<dl>

### -field UniqueConnectionId

<dd>
<p>The connection identifier (ID) that the operating system and application software use to uniquely identify the connection. The <a href="storage.logintotarget">LoginToTarget</a> and <a href="storage.addconnectiontosession">AddConnectionToSession</a> methods both return this value in the <i>UniqueConnectionId</i> parameter. Do not confuse this value with the connection ID (CID).</p>
</dd>

### -field CID

<dd>
<p>The iSCSI connection ID (CID) for this connection instance. The iSCSI protocol uses this value to identify the connection.</p>
</dd>

### -field State

<dd>
<p>The type of connection state. This member can have the following symbolic constant values, which are defined in <i>Iscsimgt.h</i>.</p>
<table>
<tr>
<th>State</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>login</p>
</td>
<td>
<p>The TCP connection has been established, but the target still has not sent a valid logon response with the final bit set. </p>
</td>
</tr>
<tr>
<td>
<p>full</p>
</td>
<td>
<p>The target has sent a valid logon response with the final bit set, and the connection is in the full feature phase. The initiator can send SCSI commands and data to targets. </p>
</td>
</tr>
<tr>
<td>
<p>logout</p>
</td>
<td>
<p>The initiator has sent a valid logoff command, but the connection has not yet been closed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Protocol

<dd>
<p>The transport protocol that is used to establish this connection instance. For a list of values that you can assign to this member, see <a href="storage.iscsi_connection_protocol_type_qualifiers">ISCSI_CONNECTION_PROTOCOL_TYPE_QUALIFIERS</a>.</p>
</dd>

### -field HeaderIntegrity

<dd>
<p>The name of the iSCSI header digest scheme that is associated with this connection session. This member can have the following symbolic constant values, which are defined in <i>Iscsimgt.h</i>.</p>
<table>
<tr>
<th>HeaderIntegrity</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>None</p>
</td>
<td>
<p>The session is not using a header digest. </p>
</td>
</tr>
<tr>
<td>
<p>crc32c</p>
</td>
<td>
<p>The session is using a 32-bit CRC digest.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field DataIntegrity

<dd>
<p>The name of the iSCSI data digest scheme that is associated with this connection session. This member can have the following symbolic constant values, which are defined in <i>Iscsimgt.h</i>.</p>
<table>
<tr>
<th>HeaderIntegrity</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>None</p>
</td>
<td>
<p>The session is not using a data digest. </p>
</td>
</tr>
<tr>
<td>
<p>crc32c</p>
</td>
<td>
<p>The session is using a 32-bit CRC digest.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Reserved

<dd>
<p>Reserved for Microsoft use only. You must set this member to 0.</p>
</dd>

### -field MaxRecvDataSegmentLength

<dd>
<p>The maximum data payload size, in bytes, that is supported for command or data PDUs within this connection session.</p>
</dd>

### -field AuthType

<dd>
<p>The type of authentication that is used to establish a connection. The <a href="storage.iscsi_connectionstaticinfo_wmi_class">ISCSI_ConnectionStaticInfo WMI Class</a>, which is defined in <i>Mgmt.mof</i>, does specify values for this member; but if your software includes <i>Iscsidsc.h</i>, it can use the <a href="storage.iscsi_auth_types">ISCSI_AUTH_TYPES</a> enumeration to assign values to this member.</p>
</dd>

### -field LocalAddr

<dd>
<p>A <a href="..\iscsidef\ns-iscsidef--iscsi-ip-address.md">ISCSI_IP_Address</a> structure that holds the IP address of the local network card that the initiator uses to connect to the network.</p>
</dd>

### -field LocalPort

<dd>
<p>The local port number that this connection instance uses.</p>
</dd>

### -field RemoteAddr

<dd>
<p>A <a href="..\iscsidef\ns-iscsidef--iscsi-ip-address.md">ISCSI_IP_Address</a> structure that holds the IP address of the remote network card that this connection instance uses.</p>
</dd>

### -field RemotePort

<dd>
<p>The remote port number that the initiator used to make the connection.</p>
</dd>

### -field EstimatedThroughput

<dd>
<p>The estimated throughput, in bytes per second, of the connection.</p>
</dd>

### -field MaxDatagramSize

<dd>
<p>The maximum size, in bytes, of the datagram that the transport supports.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsimgt.h (include Iscsimgt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.addconnectiontosession">AddConnectionToSession</a>
</dt>
<dt>
<a href="storage.iscsi_auth_types">ISCSI_AUTH_TYPES</a>
</dt>
<dt>
<a href="storage.iscsi_connection_protocol_type_qualifiers">ISCSI_CONNECTION_PROTOCOL_TYPE_QUALIFIERS</a>
</dt>
<dt>
<a href="storage.iscsi_connectionstaticinfo_wmi_class">ISCSI_ConnectionStaticInfo WMI Class</a>
</dt>
<dt>
<a href="..\iscsidef\ns-iscsidef--iscsi-ip-address.md">ISCSI_IP_Address</a>
</dt>
<dt>
<a href="storage.logintotarget">LoginToTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ISCSI_ConnectionStaticInfo structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
