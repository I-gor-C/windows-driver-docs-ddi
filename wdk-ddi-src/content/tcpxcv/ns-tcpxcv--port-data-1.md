---
UID: NS.tcpxcv._PORT_DATA_1
title: PORT_DATA_1
author: windows-driver-content
description: The XcvData function uses a PORT_DATA_1 structure when it adds a port or configures an existing port.
old-location: print\port_data_1.htm
old-project: print
ms.assetid: 6d2165a7-ee21-4f7d-a03c-f9bed87a3c7a
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PORT_DATA_1, PORT_DATA_1, *PPORT_DATA_1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: tcpxcv.h
req.include-header: Tcpxcv.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PORT_DATA_1
req.alt-loc: tcpxcv.h
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

# PORT_DATA_1 structure



## -description
<p>The <a href="print.xcvdata">XcvData</a> function uses a PORT_DATA_1 structure when it adds a port or configures an existing port.</p>


## -syntax

````
typedef struct _PORT_DATA_1 {
  WCHAR sztPortName[MAX_PORTNAME_LEN];
  DWORD dwVersion;
  DWORD dwProtocol;
  DWORD cbSize;
  DWORD dwReserved;
  WCHAR sztHostAddress[MAX_NETWORKNAME_LEN];
  WCHAR sztSNMPCommunity[MAX_SNMP_COMMUNITY_STR_LEN];
  DWORD dwDoubleSpool;
  WCHAR sztQueue[MAX_QUEUENAME_LEN];
  WCHAR sztIPAddress[MAX_IPADDR_STR_LEN];
  BYTE  Reserved[540];
  DWORD dwPortNumber;
  DWORD dwSNMPEnabled;
  DWORD dwSNMPDevIndex;
} PORT_DATA_1, *PPORT_DATA_1;
````


## -struct-fields
<dl>

### -field sztPortName

<dd>
<p>Specifies the name of the port. The MAX_PORTNAME_LEN constant is defined in tcpxcv.h.</p>
</dd>

### -field dwVersion

<dd>
<p>Specifies the version number of the PORT_DATA_1 structure, which is currently 1.</p>
</dd>

### -field dwProtocol

<dd>
<p>Specifies the protocol to use for the port. This value can be either PROTOCOL_RAWTCP_TYPE or PROTOCOL_LPR_TYPE, constants that are defined in tcpxcv.h.</p>
</dd>

### -field cbSize

<dd>
<p>Specifies the size, in bytes of this structure. Use <b>sizeof</b>(PORT_DATA_1) for this value.</p>
</dd>

### -field dwReserved

<dd>
<p>Reserved, must be set to zero.</p>
</dd>

### -field sztHostAddress

<dd>
<p>Specifies the IP Address or host name of the printer. The MAX_NETWORKNAME_LEN constant is defined in tcpxcv.h.</p>
</dd>

### -field sztSNMPCommunity

<dd>
<p>Specifies the SNMP community name of the printer. The MAX_SNMP_COMMUNITY_STR_LEN constant is defined in tcpxcv.h.</p>
</dd>

### -field dwDoubleSpool

<dd>
<p>If <b>TRUE</b>, indicates that double spooling is enabled. If <b>FALSE</b>, double spooling is disabled.</p>
</dd>

### -field sztQueue

<dd>
<p>Specifies the LPR queue name. The MAX_QUEUENAME_LEN constant is defined in tcpxcv.h.</p>
</dd>

### -field sztIPAddress

<dd>
<p>Specifies the IP address of the printer. The MAX_IPADDR_STR_LEN constant is defined in tcpxcv.h.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved, must be set to zero.</p>
</dd>

### -field dwPortNumber

<dd>
<p>Specifies the port number of the device.</p>
</dd>

### -field dwSNMPEnabled

<dd>
<p>If <b>TRUE</b>, indicates that the device supports Simple Network Management Protocol (SNMP).</p>
</dd>

### -field dwSNMPDevIndex

<dd>
<p>Specifies the SNMP device index.</p>
</dd>
</dl>

## -remarks
<p>When the <a href="print.xcvdata">XcvData</a> function is called either to add a port or configure an existing port, its <i>pOutputData</i> parameter must be set with the address of a PORT_DATA_1 structure, which will be filled in when the function returns. To add a port, set this function's <i>pszDataName</i> parameter to the string L"AddPort". To configure a port, set this parameter to L"ConfigPort". </p>

<p>See <a href="https://msdn.microsoft.com/7b2b1cff-ab8f-44e0-9327-dc60a0072bf5">TCPMON Xcv Interface</a> for more information.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Tcpxcv.h (include Tcpxcv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.xcvdata">XcvData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20PORT_DATA_1 structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
