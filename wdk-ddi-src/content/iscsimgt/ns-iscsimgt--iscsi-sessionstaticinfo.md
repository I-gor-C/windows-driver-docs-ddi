---
UID: NS.iscsimgt._ISCSI_SessionStaticInfo
title: ISCSI_SessionStaticInfo
author: windows-driver-content
description: The ISCSI_SessionStaticInfo structure provides information about the characteristics of an iSCSI session.
old-location: storage\iscsi_sessionstaticinfo.htm
old-project: storage
ms.assetid: c652268f-4a31-4ec1-a668-8700cb7f4e1b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ISCSI_SessionStaticInfo, ISCSI_SessionStaticInfo, *PISCSI_SessionStaticInfo
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
req.alt-api: ISCSI_SessionStaticInfo
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

# ISCSI_SessionStaticInfo structure



## -description
<p>The ISCSI_SessionStaticInfo structure provides information about the characteristics of an iSCSI session.</p>


## -syntax

````
typedef struct _ISCSI_SessionStaticInfo {
  ULONGLONG                  UniqueSessionId;
  WCHAR                      InitiatoriSCSIName[223 + 1];
  WCHAR                      TargetiSCSIName[223 + 1];
  USHORT                     TSID;
  UCHAR                      ISID[6];
  BOOLEAN                    InitialR2t;
  BOOLEAN                    ImmediateData;
  UCHAR                      Type;
  BOOLEAN                    DataSequenceInOrder;
  BOOLEAN                    DataPduInOrder;
  UCHAR                      ErrorRecoveryLevel;
  ULONG                      MaxOutstandingR2t;
  ULONG                      FirstBurstLength;
  ULONG                      MaxBurstLength;
  ULONG                      MaxConnections;
  USHORT                     ConnectionCount;
  ISCSI_ConnectionStaticInfo ConnectionsList[1];
} ISCSI_SessionStaticInfo, *PISCSI_SessionStaticInfo;
````


## -struct-fields
<dl>

### -field <b>UniqueSessionId</b>

<dd>
<p>A 64-bit integer that uniquely identifies the session. The <a href="storage.logintotarget">LoginToTarget</a> and <a href="storage.addconnectiontosession">AddConnectionToSession</a> methods both return this value in their UniqueSessionId parameter. Do not confuse this value with the values in the <b>ISID</b> and <b>TSID</b> members.</p>
</dd>

### -field <b>InitiatoriSCSIName</b>

<dd>
<p>A wide character string that specifies the initiator node name.</p>
</dd>

### -field <b>TargetiSCSIName</b>

<dd>
<p>A wide character string that specifies the node name of the target.</p>
</dd>

### -field <b>TSID</b>

<dd>
<p>An internal value that specifies the portion of the iSCSI session ID that the target provides. The iSCSI protocol uses TSID together with ISID to identify the session. Do not confuse TSID with the session ID that <b>UniqueSessionId</b> specifies.</p>
</dd>

### -field <b>ISID</b>

<dd>
<p>An internal value that specifies the portion of the iSCSI session ID that the initiator provides.</p>
</dd>

### -field <b>InitialR2t</b>

<dd>
<p>A Boolean value that indicates if the initiator must wait for a ready-to-send (R2T) request before sending data to the target. If this member is <b>TRUE</b>, the initiator must wait for a ready-to-send (R2T) request before sending data to the target. If this member is <b>FALSE</b>, the initiator can send unsolicited data within limits that the value of <b>FirstBurstLength</b> specifies.</p>
</dd>

### -field <b>ImmediateData</b>

<dd>
<p>A Boolean value that indicates if the initiator and target have agreed to allow the transmission of immediate data in the session. (<i>Immediate data</i> is data that the initiator piggybacks onto an iSCSI command PDU.) If this member is <b>TRUE</b>, the initiator and target have agreed to allow the transmission of immediate data in this session.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>An <a href="storage.iscsi_session_type_qualifiers">ISCSI_SESSION_TYPE_QUALIFIERS</a> enumeration value that specifies the type of logon session.</p>
<table>
<tr>
<th>Type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>discoverySession</p>
</td>
<td>
<p>Session is being used only for discovery.</p>
</td>
</tr>
<tr>
<td>
<p>informationtalSession</p>
</td>
<td>
<p>Session is being used for a limited set of SCSI commands.</p>
</td>
</tr>
<tr>
<td>
<p>dataSession</p>
</td>
<td>
<p>Session is being used as a full feature session.</p>
</td>
</tr>
<tr>
<td>
<p>bootSession</p>
</td>
<td>
<p>Session is being used to boot from target.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DataSequenceInOrder</b>

<dd>
<p>A Boolean value that indicates whether sequences of data PDUs must be transmitted by using continuously increasing offsets, except during error recovery. If this member is <b>TRUE</b>, sequences of data PDUs must be transmitted by using continuously increasing offsets, except during error recovery. If this member is <b>FALSE</b>, sequences of data PDUs can be transmitted in any order. </p>
<p>The value in <b>DataSequenceInOrder</b> indicates the ordering of the sequences themselves, not the ordering of the data PDUs within each sequence. The <b>DataPduInOrder</b> member indicates the ordering of the data PDUs within each sequence. </p>
</dd>

### -field <b>DataPduInOrder</b>

<dd>
<p>A Boolean value that indicates whether the data PDUs within a sequence of data PDUs must be located at continuously increasing addresses. If this member is <b>TRUE</b>, the data PDUs within a sequence of data PDUs must be located at continuously increasing addresses, with no gaps or overlay between PDUs. If this member is <b>FALSE</b>, the data PDUs within each sequence can be in any order. </p>
</dd>

### -field <b>ErrorRecoveryLevel</b>

<dd>
<p>The level of error recovery that the initiator and the target negotiated. Higher numbers represent more elaborate recovery schemes. Currently, this member must be 0 or ULONG_VALUE_UNKNOWN.</p>
</dd>

### -field <b>MaxOutstandingR2t</b>

<dd>
<p>The maximum number of outstanding ready-to-transmit (R2T) requests that are allowed for each task within this session. </p>
</dd>

### -field <b>FirstBurstLength</b>

<dd>
<p>The maximum amount of unsolicited data, in bytes, that you can send within this session. </p>
</dd>

### -field <b>MaxBurstLength</b>

<dd>
<p>The maximum number of bytes that you can send within a single sequence of Data-In or Data-Out PDUs. </p>
</dd>

### -field <b>MaxConnections</b>

<dd>
<p>The maximum number of connections that are allowed within this session.</p>
</dd>

### -field <b>ConnectionCount</b>

<dd>
<p>The number of connections that currently belong to this session.</p>
</dd>

### -field <b>ConnectionsList</b>

<dd>
<p>A variable length array of <a href="..\iscsimgt\ns-iscsimgt--iscsi-connectionstaticinfo.md">ISCSI_ConnectionStaticInfo</a> structures that specifies the static configuration data for each connection that is associated with this session. <b>ConnectionCount</b> indicates the number of elements in the array.</p>
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
<a href="..\iscsimgt\ns-iscsimgt--iscsi-connectionstaticinfo.md">ISCSI_ConnectionStaticInfo</a>
</dt>
<dt>
<a href="storage.loginsessiontype">LOGINSESSIONTYPE</a>
</dt>
<dt>
<a href="storage.logintotarget">LoginToTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ISCSI_SessionStaticInfo structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
