---
UID: NC.wsk.PFN_WSK_GET_NAME_INFO
title: PFN_WSK_GET_NAME_INFO
author: windows-driver-content
description: The WskGetNameInfo function provides protocol-independent translation from a transport address to a host name.
old-location: netvista\wskgetnameinfo.htm
old-project: netvista
ms.assetid: 99e10a70-90a7-4d96-ae5f-ba82d8c4c1a8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskGetNameInfo
req.alt-loc: wsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PFN_WSK_GET_NAME_INFO callback



## -description
<p>The 
  <b>WskGetNameInfo</b> function provides protocol-independent translation from a transport address to a host
  name.</p>


## -prototype

````
NTSTATUS WSKAPI * WskGetNameInfo(
  _In_      PWSK_CLIENT     Client,
  _In_      PSOCKADDR       SockAddr,
  _In_      ULONG           SockAddrLength,
  _Out_opt_ PUNICODE_STRING NodeName,
  _Out_opt_ PUNICODE_STRING ServiceName,
  _In_      ULONG           Flags,
  _In_opt_  PEPROCESS       OwningProcess,
  _In_opt_  PETHREAD        OwningThread,
  _Inout_   PIRP            Irp
);
````


## -parameters
<dl>

### -param Client [in]

<dd>
<p>[in] A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571155">WSK_CLIENT</a> structure that was returned through
     the 
     <i>WskProviderNpi</i> parameter of the 
     <a href="..\wsk\nf-wsk-wskcaptureprovidernpi.md">
     WskCaptureProviderNPI</a> function.</p>
</dd>

### -param SockAddr [in]

<dd>
<p>[in] A pointer to a 
     <a href="netvista.sockaddr">SOCKADDR</a> structure that contains the IP address
     and port number of the socket.</p>
</dd>

### -param SockAddrLength [in]

<dd>
<p>[in] Specifies the length, in bytes, of the buffer pointed to by the 
     <i>SockAddr</i> parameter. The value of 
     <i>SockAddrLength</i> should not exceed the size of the 
     <a href="..\ntifs\ns-ntifs-sockaddr-storage.md">SOCKADDR_STORAGE</a> structure.</p>
</dd>

### -param NodeName [out, optional]

<dd>
<p>[out] An optional pointer to a 
     <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains a
     Unicode string that represents a host (node) name. On success, the Unicode host name is written as a
     Fully Qualified Domain Name (FQDN) by default. The caller must provide a UNICODE_STRING buffer large
     enough to hold the Unicode host name, which includes the terminating NULL character. If the 
     <i>NodeBuffer</i> parameter is <b>NULL</b>, the caller does not want to receive a host name string. 
     <i>NodeBuffer</i> and 
     <i>ServiceBuffer</i> must not both be <b>NULL</b>.</p>
</dd>

### -param ServiceName [out, optional]

<dd>
<p>[out] An optional pointer to a 
     <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains a
     Unicode string that represents a service name associated with the port number. The caller must provide a
     UNICODE_STRING buffer large enough to hold the Unicode service name, which includes the terminating NULL
     character. If the 
     <i>NodeBuffer</i> parameter is <b>NULL</b>, the caller does not want to receive a service name string. 
     <i>NodeBuffer</i> and 
     <i>ServiceBuffer</i> must not both be <b>NULL</b>.</p>
</dd>

### -param Flags [in]

<dd>
<p>[in] A ULONG value that is used to customize the processing of this function.
     </p>
<p>The following flags are available:</p>
<p></p>
<dl>

### -param NI_DGRAM

<dd>
<p>Indicates that the service is a datagram service. This flag is necessary for the few services
       that provide different port numbers for UDP and TCP service.</p>
</dd>

### -param NI_NAMEREQD

<dd>
<p>Indicates that a host name that cannot be resolved by DNS results in an error.</p>
</dd>

### -param NI_NOFQDN

<dd>
<p>Results in a local host having only its Relative Distinguished Name (RDN) returned in the 
       <i>NodeName</i> parameter.</p>
</dd>

### -param NI_NUMERICHOST

<dd>
<p>Indicates that the function returns the numeric form of the host name instead of its name, a
       reverse DNS lookup. The numeric form of the host name is also returned if the host name cannot be
       resolved by DNS.</p>
</dd>

### -param NI_NUMERICSERV

<dd>
<p>Indicates that the function returns the port number of the service instead of its name. Also, if
       a host name is not found for an IP address (127.0.0.2, for example), the host name is returned as the
       IP address.</p>
</dd>
</dl>
</dd>

### -param OwningProcess [in, optional]

<dd>
<p>[in] An optional pointer to the process from which the function retrieves the security context.
     This security context indicates the user account context in which the function processes the name
     resolution request.
     </p>
<p>If this parameter is <b>NULL</b>, the function processes the name resolution request in the context of a
     predefined local account with minimal privileges.</p>
<p>If this parameter is not <b>NULL</b> and an impersonation token is in effect for the calling thread, this
     function fails and returns STATUS_INVALID_PARAMETER.</p>
</dd>

### -param OwningThread [in, optional]

<dd>
<p>[in] An optional pointer to the thread from which the function retrieves the security context.
     This parameter can be non-<b>NULL</b> only if 
     <i>OwningProcess</i> is non-<b>NULL</b>. Otherwise, this function fails and returns STATUS_INVALID_PARAMETER.
     </p>
<p>If this parameter is not <b>NULL</b> and an impersonation token is in effect for the calling thread, this
     function fails and returns STATUS_INVALID_PARAMETER.</p>
</dd>

### -param Irp [in, out]

<dd>
<p>[in/out] A pointer to an I/O request packet (IRP) to use to complete the request asynchronously.
     Upon completion of the request, 
     <i>Irp</i> -&gt;
     <b>Iostatus.Information</b> will hold the returned status code.</p>
</dd>
</dl>

## -returns
<p><b>WskGetNameInfo</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was specified.</p><dl>
<dt><b>STATUS_NO_MATCH</b></dt>
</dl><p>The host name cannot be resolved.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function completed successfully. If the WSK application specified a pointer to an IRP in the
       
       <i>Irp</i> parameter, the IRP will be completed with a success status.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK subsystem could not complete the function immediately. The WSK subsystem will complete
       the IRP after it has completed the control operation. The status of the control operation will be
       returned in the 
       <b>IoStatus.Status</b> field of the IRP.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. The IRP will be completed with failure status.</p>

<p> </p>

## -remarks
<p>The process to which the 
    <i>OwningProcess</i> parameter points, or the thread to which the 
    <i>OwningThread</i> process points, indicates the security context for this function. The user account
    that is indicated by the security context indicates the context for the function's name resolution
    request.</p>

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
<p>Available in Windows 7 and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wsk.h (include Wsk.h)</dt>
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
<a href="netvista.sockaddr">SOCKADDR</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs-sockaddr-storage.md">SOCKADDR_STORAGE</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571155">WSK_CLIENT</a>
</dt>
<dt>
<a href="..\wsk\nf-wsk-wskcaptureprovidernpi.md">WskCaptureProviderNPI</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-get-address-info.md">WskGetAddressInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_GET_NAME_INFO callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
