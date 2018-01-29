---
UID : NC:wsk.PFN_WSK_GET_NAME_INFO
title : PFN_WSK_GET_NAME_INFO
author : windows-driver-content
description : The WskGetNameInfo function provides protocol-independent translation from a transport address to a host name.
old-location : netvista\wskgetnameinfo.htm
old-project : netvista
ms.assetid : 99e10a70-90a7-4d96-ae5f-ba82d8c4c1a8
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.wskgetnameinfo, WskGetNameInfo callback function [Network Drivers Starting with Windows Vista], WskGetNameInfo, PFN_WSK_GET_NAME_INFO, PFN_WSK_GET_NAME_INFO, wsk/WskGetNameInfo, wskref_cebad0ad-55bc-4fae-9c73-5a501417ea5c.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wsk.h
req.include-header : Wsk.h
req.target-type : Universal
req.target-min-winverclnt : Available in Windows 7 and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WNODE_HEADER, *PWNODE_HEADER
req.product : Windows 10 or later.
---


# PFN_WSK_GET_NAME_INFO callback function
The 
  <b>WskGetNameInfo</b> function provides protocol-independent translation from a transport address to a host
  name.

## Syntax

```
PFN_WSK_GET_NAME_INFO PfnWskGetNameInfo;

NTSTATUS PfnWskGetNameInfo(
  PWSK_CLIENT Client,
  PSOCKADDR SockAddr,
  ULONG SockAddrLength,
  PUNICODE_STRING NodeName,
  PUNICODE_STRING ServiceName,
  ULONG Flags,
  PEPROCESS OwningProcess,
  PETHREAD OwningThread,
  PIRP Irp
)
{...}
```

## Parameters

`Client`

[in] A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571155">WSK_CLIENT</a> structure that was returned through
     the 
     <i>WskProviderNpi</i> parameter of the 
     <mshelp:link keywords="netvista.wskcaptureprovidernpi" tabindex="0"><b>
     WskCaptureProviderNPI</b></mshelp:link> function.

`SockAddr`

[in] A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff570822">SOCKADDR</a> structure that contains the IP address
     and port number of the socket.

`SockAddrLength`

[in] Specifies the length, in bytes, of the buffer pointed to by the 
     <i>SockAddr</i> parameter. The value of 
     <i>SockAddrLength</i> should not exceed the size of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff570825">SOCKADDR_STORAGE</a> structure.

`NodeName`

[out] An optional pointer to a 
     <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure that contains a
     Unicode string that represents a host (node) name. On success, the Unicode host name is written as a
     Fully Qualified Domain Name (FQDN) by default. The caller must provide a UNICODE_STRING buffer large
     enough to hold the Unicode host name, which includes the terminating NULL character. If the 
     <i>NodeBuffer</i> parameter is <b>NULL</b>, the caller does not want to receive a host name string. 
     <i>NodeBuffer</i> and 
     <i>ServiceBuffer</i> must not both be <b>NULL</b>.

`ServiceName`

[out] An optional pointer to a 
     <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure that contains a
     Unicode string that represents a service name associated with the port number. The caller must provide a
     UNICODE_STRING buffer large enough to hold the Unicode service name, which includes the terminating NULL
     character. If the 
     <i>NodeBuffer</i> parameter is <b>NULL</b>, the caller does not want to receive a service name string. 
     <i>NodeBuffer</i> and 
     <i>ServiceBuffer</i> must not both be <b>NULL</b>.

`Flags`

[in] A ULONG value that is used to customize the processing of this function.
     

The following flags are available:

`OwningProcess`

[in] An optional pointer to the process from which the function retrieves the security context.
     This security context indicates the user account context in which the function processes the name
     resolution request.
     

If this parameter is <b>NULL</b>, the function processes the name resolution request in the context of a
     predefined local account with minimal privileges.

If this parameter is not <b>NULL</b> and an impersonation token is in effect for the calling thread, this
     function fails and returns STATUS_INVALID_PARAMETER.

`OwningThread`

[in] An optional pointer to the thread from which the function retrieves the security context.
     This parameter can be non-<b>NULL</b> only if 
     <i>OwningProcess</i> is non-<b>NULL</b>. Otherwise, this function fails and returns STATUS_INVALID_PARAMETER.
     

If this parameter is not <b>NULL</b> and an impersonation token is in effect for the calling thread, this
     function fails and returns STATUS_INVALID_PARAMETER.

`Irp`

[in/out] A pointer to an I/O request packet (IRP) to use to complete the request asynchronously.
     Upon completion of the request, 
     <i>Irp</i> -&gt;
     <b>Iostatus.Information</b> will hold the returned status code.


## Return Value

<b>WskGetNameInfo</b> returns one of the following NTSTATUS codes:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
An invalid parameter was specified.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NO_MATCH</b></dt>
</dl>
</td>
<td width="60%">
The host name cannot be resolved.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The function completed successfully. If the WSK application specified a pointer to an IRP in the
       
       <i>Irp</i> parameter, the IRP will be completed with a success status.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_PENDING</b></dt>
</dl>
</td>
<td width="60%">
The WSK subsystem could not complete the function immediately. The WSK subsystem will complete
       the IRP after it has completed the control operation. The status of the control operation will be
       returned in the 
       <b>IoStatus.Status</b> field of the IRP.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>Other status codes</b></dt>
</dl>
</td>
<td width="60%">
An error occurred. The IRP will be completed with failure status.

</td>
</tr>
</table>

## Remarks

The process to which the 
    <i>OwningProcess</i> parameter points, or the thread to which the 
    <i>OwningThread</i> process points, indicates the security context for this function. The user account
    that is indicated by the security context indicates the context for the function's name resolution
    request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wsk.h (include Wsk.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff570822">SOCKADDR</a>

<a href="..\wsk\nf-wsk-wskcaptureprovidernpi.md">WskCaptureProviderNPI</a>

<a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571155">WSK_CLIENT</a>

<a href="..\wsk\nc-wsk-pfn_wsk_get_address_info.md">WskGetAddressInfo</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff570825">SOCKADDR_STORAGE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_GET_NAME_INFO callback function%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>