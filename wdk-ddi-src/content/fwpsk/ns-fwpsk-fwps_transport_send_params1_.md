---
UID: NS.FWPSK.FWPS_TRANSPORT_SEND_PARAMS1_
title: FWPS_TRANSPORT_SEND_PARAMS1_
author: windows-driver-content
description: The FWPS_TRANSPORT_SEND_PARAMS1 structure defines properties of an outbound transport layer packet.Note  FWPS_TRANSPORT_SEND_PARAMS1 is the specific version of FWPS_TRANSPORT_SEND_PARAMS used in Windows 7 and later.
old-location: netvista\fwps_transport_send_params1.htm
old-project: NetVista
ms.assetid: 8d5653e4-a755-4066-b25a-f8f589821412
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FWPS_TRANSPORT_SEND_PARAMS1_, FWPS_TRANSPORT_SEND_PARAMS1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_TRANSPORT_SEND_PARAMS1
req.alt-loc: fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# FWPS_TRANSPORT_SEND_PARAMS1_ structure



## -description
The <b>FWPS_TRANSPORT_SEND_PARAMS1</b> structure defines properties of an outbound transport layer
  packet.



## -syntax

````
typedef struct FWPS_TRANSPORT_SEND_PARAMS1_ {
  UCHAR      *remoteAddress;
  SCOPE_ID   remoteScopeId;
  WSACMSGHDR *controlData;
  ULONG      controlDataLength;
  UCHAR      *headerIncludeHeader;
  ULONG      headerIncludeHeaderLength;
} FWPS_TRANSPORT_SEND_PARAMS1;
````


## -struct-fields

### -field remoteAddress

A pointer to a buffer that specifies the remote IP address to which the socket needs to be sent.
     The remote address specified by this member can be different than the one passed as one of the incoming
     data values to the callout driver's 
     <a href="netvista.classifyfn">classifyFn</a> callout function.
     

The buffer can contain an IPv4 address (4 bytes) or an IPv6 address (16 bytes), and the address must
     be specified in network byte order. The IP version must match the 
     <i>AddressFamily</i> parameter specified in the 
     <a href="netvista.fwpsinjecttransportsendasync1">
     FwpsInjectTransportSendAsync1</a> function.

The buffer must remain valid until the injection completion function is called.


### -field remoteScopeId

A <b>SCOPE_ID</b> structure that contains the scope identifier for the remote IP address. The scope
     identifier is provided to a callout through the 
     <b>remoteScopeId</b> member of the 
     <a href="netvista.fwps_incoming_metadata_values0">
     FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
     <a href="netvista.classifyfn">classifyFn</a> callout function. The <b>SCOPE_ID</b>
     structure is defined in 
     Ws2ipdef.h as follows.

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct {
  union {
    struct {
      ULONG  Zone : 28;
      ULONG  Level : 4;
    };
    ULONG  Value;
  };
} SCOPE_ID, *PSCOPE_ID;</pre>
</td>
</tr>
</table></span></div>

### -field controlData

An optional pointer to a buffer that contains socket control data specified by the 
      <a href="winsock.wsasendmsg">WSASendMsg</a> function. For information about the <b>WSACMSGHDR</b> type, see 
      <a href="netvista.cmsghdr">CMSGHDR</a>.

If present, socket control data is provided to a callout with the 
      <b>controlData</b> member of the 
      <a href="netvista.fwps_incoming_metadata_values0">
      FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
      <a href="netvista.classifyfn">classifyFn</a> callout function.

If socket control data is not <b>NULL</b>, it must be deep-copied in the callout driver's implementation
      of the 
      <a href="netvista.classifyfn">classifyFn</a> function, and the 
      <b>controlData</b> buffer must be kept valid until the injection completion
      function is called.


### -field controlDataLength

The length, in bytes, of the 
     <b>controlData</b> member.


### -field headerIncludeHeader

The transport header to include.


### -field headerIncludeHeaderLength

The length, in bytes, of the 
     <b>headerIncludeHeader</b> member.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 7.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.classifyfn">classifyFn</a>
</dt>
<dt>
<a href="netvista.cmsghdr">CMSGHDR</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_metadata_values0">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="netvista.fwpsinjecttransportsendasync1">
   FwpsInjectTransportSendAsync1</a>
</dt>
<dt>
<a href="winsock.wsasendmsg">WSASendMsg</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20FWPS_TRANSPORT_SEND_PARAMS1 structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

