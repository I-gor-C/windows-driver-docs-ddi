---
UID: NC.wsk.PFN_WSK_CONTROL_SOCKET
title: PFN_WSK_CONTROL_SOCKET
author: windows-driver-content
description: The WskControlSocket function performs control operations on a socket.
old-location: netvista\wskcontrolsocket.htm
old-project: netvista
ms.assetid: d65fd2ab-ffca-4e13-b0f1-42d6a89f4b4a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskControlSocket
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
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# PFN_WSK_CONTROL_SOCKET callback



## -description
<p>The 
  <b>WskControlSocket</b> function performs control operations on a socket.</p>


## -prototype

````
NTSTATUS WSKAPI * WskControlSocket(
  _In_      PWSK_SOCKET             Socket,
  _In_      WSK_CONTROL_SOCKET_TYPE RequestType,
  _In_      ULONG                   ControlCode,
  _In_      ULONG                   Level,
  _In_      SIZE_T                  InputSize,
  _In_opt_  PVOID                   InputBuffer,
  _In_      SIZE_T                  OutputSize,
  _Out_opt_ PVOID                   OutputBuffer,
  _Out_opt_ SIZE_T                  *OutputSizeReturned,
  _Inout_   PIRP                    Irp
);
````


## -parameters
<dl>

### -param Socket [in]

<dd>
<p>A pointer to a 
     <a href="..\wsk\ns-wsk--wsk-socket.md">WSK_SOCKET</a> structure that specifies the socket
     object for the socket on which the control operation is being performed.</p>
</dd>

### -param RequestType [in]

<dd>
<p>A value that specifies the type of control operation that is being performed. A WSK application
     sets this parameter to one of the following values:
     </p>
<p></p>
<dl>

### -param WskSetOption

<dd>
<p>Set the state or value for a socket option.</p>
</dd>

### -param WskGetOption

<dd>
<p>Get the state or value of a socket option.</p>
</dd>

### -param WskIoctl

<dd>
<p>Perform an I/O control operation.</p>
</dd>
</dl>
</dd>

### -param ControlCode [in]

<dd>
<p>If the 
     <i>RequestType</i> parameter is set to 
     <b>WskSetOption</b> or 
     <b>WskGetOption</b>, the 
     <i>ControlCode</i> parameter specifies the particular socket option whose value is being set or
     retrieved. For more information about socket options that are supported by the WSK subsystem, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571186">WSK Socket Options</a>. The underlying
     network protocol might support additional socket options.
     </p>
<p>If the 
     <i>RequestType</i> parameter is set to 
     <b>WskIoctl</b>, the 
     <i>ControlCode</i> parameter specifies the particular I/O control operation that is being performed. For
     more information about I/O control operations that are supported by the WSK subsystem, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571183">WSK Socket IOCTL Operations</a>. The
     underlying network protocol might support additional socket I/O control operations.</p>
</dd>

### -param Level [in]

<dd>
<p>The level in the network stack at which the value for a socket option is being either set or
     retrieved. For WSK subsystem level socket options, the WSK application should set this parameter to
     SOL_SOCKET. For transport protocol or network protocol level socket options, the WSK application should
     set this parameter to the appropriate level for the underlying transport.
     </p>
<p>If the 
     <i>RequestType</i> parameter is set to 
     <b>WskIoctl</b>, the 
     <i>Level</i> parameter is ignored.</p>
</dd>

### -param InputSize [in]

<dd>
<p>The number of bytes of data in the buffer that is pointed to by the 
     <i>InputBuffer</i> parameter.</p>
</dd>

### -param InputBuffer [in, optional]

<dd>
<p>A caller-allocated buffer that supplies any input data that is required to perform the specified
     control operation. If no input data is required for the specified control operation, the WSK application
     should set this parameter to <b>NULL</b> and set the 
     <i>InputSize</i> parameter to zero.</p>
</dd>

### -param OutputSize [in]

<dd>
<p>The size of the buffer that is pointed to by the 
     <i>OutputBuffer</i> parameter.</p>
</dd>

### -param OutputBuffer [out, optional]

<dd>
<p>A caller-allocated buffer that receives any output data that is returned by the specified control
     operation. If no output data is returned by the specified control operation, the WSK application should
     set this parameter to <b>NULL</b> and set the 
     <i>OutputSize</i> parameter to zero.</p>
</dd>

### -param OutputSizeReturned [out, optional]

<dd>
<p>A pointer to a ULONG-typed variable that receives the number of bytes of data that is returned in
     the buffer that is pointed to by the 
     <i>OutputBuffer</i> parameter. A WSK application should set the 
     <i>OutputSizeReturned</i> parameter to <b>NULL</b> except when all of the following are true:
     </p>
<ul>
<li>
<p>The 
       <i>Irp</i> parameter is set to <b>NULL</b>.</p>
</li>
<li>
<p>The operation that is being performed returns output data in the buffer that is pointed to by the 
       <i>OutputBuffer</i> parameter.</p>
</li>
<li>
<p>The number of bytes of output data that is returned by the operation that is being performed is
       unknown.</p>
</li>
</ul>
</dd>

### -param Irp [in, out]

<dd>
<p>A pointer to a caller-allocated IRP that the WSK subsystem uses to complete the control operation
     asynchronously. For more information about using IRPs with WSK functions, see 
     <a href="netvista.using_irps_with_winsock_kernel_functions">Using IRPs with Winsock
     Kernel Functions</a>.
     </p>
<p>If the 
     <i>RequestType</i> parameter is set to either 
     <b>WskSetOption</b> or 
     <b>WskGetOption</b>, the 
     <i>Irp</i> parameter is required, is optional, or must be <b>NULL</b> depending on the particular socket option
     that is being set or retrieved. For more information about the requirements for the 
     <i>Irp</i> parameter for each of the supported socket options, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571186">WSK Socket Options</a>.</p>
<p>If the 
     <i>RequestType</i> parameter is set to 
     <b>WskIoctl</b>, the 
     <i>Irp</i> parameter is required, is optional, or must be <b>NULL</b> depending on the particular I/O control
     operation that is being performed. For more information about the requirements for the 
     <i>Irp</i> parameter for each of the supported I/O control operations, see 
     <a href="netvista.wsk_socket_ioctl_operations">WSK Socket IOCTL
     Operations</a>.</p>
</dd>
</dl>

## -returns
<p><b>WskControlSocket</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The control operation completed successfully. If the WSK application specified a pointer to an
       IRP in the 
       <i>Irp</i> parameter, the IRP will be completed with success status, and the number of bytes that is
       returned in the buffer that is pointed to by the 
       <i>OutputBuffer</i> parameter will be returned in the 
       <b>IoStatus.Information</b> field of the IRP.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The WSK subsystem could not complete the control operation immediately. The WSK subsystem will
       complete the IRP after it has completed the control operation. The status of the control operation
       will be returned in the 
       <b>IoStatus.Status</b> field of the IRP. If the operation succeeds, the number of bytes that is
       returned in the buffer that is pointed to by the 
       <i>OutputBuffer</i> parameter will be returned in the 
       <b>IoStatus.Information</b> field of the IRP.</p><dl>
<dt><b>STATUS_EVENT_PENDING</b></dt>
</dl><p>The WSK subsystem could not complete the control operation immediately. This value is returned
       only when a WSK application is disabling an event callback function on a socket when there are
       currently in-progress calls to that event callback function and when the 
       <i>Irp</i> parameter is <b>NULL</b>. For more information about disabling event callback functions, see 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff570834">SO_WSK_EVENT_CALLBACK</a>.</p><dl>
<dt><b>STATUS_FILE_FORCED_CLOSED</b></dt>
</dl><p>The socket is no longer functional. The IRP will be completed with failure status. The WSK
       application must call the 
       <a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a> function to close the
       socket as soon as possible.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. The IRP will be completed with failure status.</p>

<p> </p>

## -remarks
<p>If a WSK application specifies 
    <b>WskSetOption</b> or 
    <b>WskGetOption</b> in the 
    <i>RequestType</i> parameter, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571186">WSK Socket Options</a> for more information
    about how the input and output buffers are used for each socket option.</p>

<p>If a WSK application specifies 
    <b>WskIoctl</b> in the 
    <i>RequestType</i> parameter, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571183">WSK Socket IOCTL Operations</a> for
    more information about how the input and output buffers are used for each I/O control operation.</p>

<p>If the 
    <b>WskControlSocket</b> function returns STATUS_PENDING, any buffers that are pointed to by the 
    <i>InputBuffer</i> parameter or the 
    <i>OutputBuffer</i> parameter must remain valid until the IRP is completed. If the WSK application
    allocated the buffers with one of the 
    <b>ExAllocate<i>Xxx</i></b> functions, it cannot free the memory with the corresponding 
    <b>ExFree<i>Xxx</i></b> function until after the IRP is completed. If the WSK application allocated the buffers on the
    stack, it cannot return from the function that calls the 
    <b>WskControlSocket</b> function until after the IRP is completed.</p>

<p>Callers of the 
    <b>WskControlSocket</b> function must be running at IRQL &lt;= DISPATCH_LEVEL except when the 
    <i>RequestType</i> parameter is set to 
    <b>WskIoctl</b> and the 
    <i>ControlCode</i> parameter is set to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570815">SIO_ADDRESS_LIST_QUERY</a>, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff570814">SIO_ADDRESS_LIST_CHANGE</a>, or <a href="winsock.using_sio_address_list_sort">SIO_ADDRESS_LIST_SORT</a>. In this
    situation, callers must be running at IRQL = PASSIVE_LEVEL.</p>

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
<dt>Wsk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-basic-dispatch.md">WSK_PROVIDER_BASIC_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-connection-dispatch.md">
   WSK_PROVIDER_CONNECTION_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-datagram-dispatch.md">
   WSK_PROVIDER_DATAGRAM_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-listen-dispatch.md">WSK_PROVIDER_LISTEN_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571183">WSK Socket IOCTL Operations</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571186">WSK Socket Options</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PFN_WSK_CONTROL_SOCKET callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
