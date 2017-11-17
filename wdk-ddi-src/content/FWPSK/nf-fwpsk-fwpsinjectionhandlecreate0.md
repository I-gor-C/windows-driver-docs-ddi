---
UID: NF.fwpsk.FwpsInjectionHandleCreate0
title: FwpsInjectionHandleCreate0
author: windows-driver-content
description: The FwpsInjectionHandleCreate0 function creates a handle that can be used by packet injection functions to inject packet or stream data into the TCP/IP network stack and by the FwpsQueryPacketInjectionState0 function to query the packet injection state.Note  FwpsInjectionHandleCreate0 is a specific version of FwpsInjectionHandleCreate. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwpsinjectionhandlecreate0.htm
ms.assetid: 61cee8ef-1070-46d4-a541-94a9f09b593b
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsInjectionHandleCreate0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: FwpsInjectionHandleCreate0
req.iface: 
---

# FwpsInjectionHandleCreate0 function



## -description
<p>The 
  <b>FwpsInjectionHandleCreate0</b> function creates a handle that can be used by 
  <a href="NULL">packet injection functions</a> to inject
  packet or stream data into the TCP/IP network stack and by the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a> function to query the packet injection state.</p>


## -syntax

````
NTSTATUS NTAPI FwpsInjectionHandleCreate0(
  _In_opt_ ADDRESS_FAMILY addressFamily,
  _In_     UINT32         flags,
  _Out_    HANDLE         *injectionHandle
);
````


## -parameters
<dl>

### -param <i>addressFamily</i> [in, optional]

<dd>
<p>The address family for which the injection handle is being created. This can be one of the
     following address families:
     </p>
<p></p>
<dl>

### -param <a id="AF_UNSPEC"></a><a id="af_unspec"></a>AF_UNSPEC

<dd>
<p>The address family is unspecified.</p>
</dd>

### -param <a id="AF_INET"></a><a id="af_inet"></a>AF_INET

<dd>
<p>The IPv4 address family.</p>
</dd>

### -param <a id="AF_INET6"></a><a id="af_inet6"></a>AF_INET6

<dd>
<p>The IPv6 address family.</p>
</dd>
</dl>
<p>For transport, stream, and forward injections, this parameter is optional and can be set to
     AF_UNSPEC, which indicates an unspecified address family. This value is defined in 
     Ws2def.h.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>A flag value set by a callout driver to indicate the type of data to be injected. This flag can have
     one or more of the following values: 
     </p>
<p></p>
<dl>

### -param <a id="FWPS_INJECTION_TYPE_FORWARD"></a><a id="fwps_injection_type_forward"></a>FWPS_INJECTION_TYPE_FORWARD

<dd>
<p>Packet data will be injected by calling the 
       <a href="https://msdn.microsoft.com/b7cb70c6-c672-4a29-983c-c73767af72ea">
       FwpsInjectForwardAsync0</a> function.</p>
</dd>

### -param <a id="FWPS_INJECTION_TYPE_NETWORK"></a><a id="fwps_injection_type_network"></a>FWPS_INJECTION_TYPE_NETWORK

<dd>
<p>Network data will be injected by calling either the 
       <a href="https://msdn.microsoft.com/c34b2be1-fe1c-4a99-ac9c-ddd40b97d8d0">
       FwpsInjectNetworkReceiveAsync0</a> function or the 
       <a href="https://msdn.microsoft.com/9cc76bf7-a744-46f9-89d5-5277744221e5">
       FwpsInjectNetworkSendAsync0</a> function.</p>
</dd>

### -param <a id="FWPS_INJECTION_TYPE_STREAM"></a><a id="fwps_injection_type_stream"></a>FWPS_INJECTION_TYPE_STREAM

<dd>
<p>Stream data will be injected by calling the 
       <a href="https://msdn.microsoft.com/d72c3067-21df-40ee-a898-100fcdc5eaca">
       FwpsStreamInjectAsync0</a> function.</p>
</dd>

### -param <a id="FWPS_INJECTION_TYPE_TRANSPORT"></a><a id="fwps_injection_type_transport"></a>FWPS_INJECTION_TYPE_TRANSPORT

<dd>
<p>Transport data will be injected by calling either the 
       <a href="https://msdn.microsoft.com/0809a013-9977-44fc-b800-576b4fd983e8">
       FwpsInjectTransportReceiveAsync0</a> function or the 
       <a href="https://msdn.microsoft.com/1298a825-16c4-49ab-b038-19247975ea46">
       FwpsInjectTransportSendAsync0</a> function.</p>
</dd>
</dl>
<p> To create an injection handle to be used by multiple injection functions, combine the
     injection type bits with bitwise OR operations. If the flag value is set to zero, the resulting
     injection handle can be used for transport, stream, and forward injections.</p>
</dd>

### -param <i>injectionHandle</i> [out]

<dd>
<p>A pointer to a variable that receives the handle.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsInjectionHandleCreate0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The injection handle was successfully created.</p><dl>
<dt><b>STATUS_FWP_TCPIP_NOT_READY</b></dt>
</dl><p>The TCP/IP network stack is not ready. A callout driver should call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a> function again at a later time to create an injection handle.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsInjectionHandleCreate0</b> function to create a handle that can be used for injecting packet or
    stream data into the TCP/IP network stack and to query the packet injection state. A callout driver
    passes the created handle to the 
    <a href="netvista.packet_injection_functions">packet injection
    functions</a> and 
    <a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
    FwpsQueryPacketInjectionState0</a>.</p>

<p>After a callout driver has finished using an injection handle, it must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551181">FwpsInjectionHandleDestroy0</a> function to destroy the handle. If pending injections have not yet
    completed, this function will wait for their completion before returning.</p>

<p>When injections are being made to the network layer and both IPv4 and IPv6 address families are being
    filtered, the callout driver must create two injection handles by calling the 
    <b>FwpsInjectionHandleCreate0</b> function twice: one call with 
    <i>addressFamily</i> set to AF_INET, and a second call with 
    <i>addressFamily</i> set to AF_INET6.</p>

<p>A callout driver calls the 
    <b>FwpsInjectionHandleCreate0</b> function to create a handle that can be used for injecting packet or
    stream data into the TCP/IP network stack and to query the packet injection state. A callout driver
    passes the created handle to the 
    <a href="netvista.packet_injection_functions">packet injection
    functions</a> and 
    <a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
    FwpsQueryPacketInjectionState0</a>.</p>

<p>After a callout driver has finished using an injection handle, it must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551181">FwpsInjectionHandleDestroy0</a> function to destroy the handle. If pending injections have not yet
    completed, this function will wait for their completion before returning.</p>

<p>When injections are being made to the network layer and both IPv4 and IPv6 address families are being
    filtered, the callout driver must create two injection handles by calling the 
    <b>FwpsInjectionHandleCreate0</b> function twice: one call with 
    <i>addressFamily</i> set to AF_INET, and a second call with 
    <i>addressFamily</i> set to AF_INET6.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551181">FwpsInjectionHandleDestroy0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
   FwpsQueryPacketInjectionState0</a>
</dt>
<dt>
<a href="NULL">Packet Injection Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsInjectionHandleCreate0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
