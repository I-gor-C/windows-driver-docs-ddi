---
UID: NF.fltkernel.FltCreateCommunicationPort
title: FltCreateCommunicationPort
author: windows-driver-content
description: FltCreateCommunicationPort creates a communication server port on which a minifilter driver can receive connection requests from user-mode applications.
old-location: ifsk\fltcreatecommunicationport.htm
old-project: ifsk
ms.assetid: 9987ed6b-7792-4035-9640-9ee9595e854a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltCreateCommunicationPort
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCreateCommunicationPort
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltCreateCommunicationPort function



## -description
<p><b>FltCreateCommunicationPort</b> creates a communication server port on which a minifilter driver can receive connection requests from user-mode applications. </p>


## -syntax

````
NTSTATUS FltCreateCommunicationPort(
  _In_     PFLT_FILTER            Filter,
  _Out_    PFLT_PORT              *ServerPort,
  _In_     POBJECT_ATTRIBUTES     ObjectAttributes,
  _In_opt_ PVOID                  ServerPortCookie,
  _In_     PFLT_CONNECT_NOTIFY    ConnectNotifyCallback,
  _In_     PFLT_DISCONNECT_NOTIFY DisconnectNotifyCallback,
  _In_opt_ PFLT_MESSAGE_NOTIFY    MessageNotifyCallback,
  _In_     LONG                   MaxConnections
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Opaque filter pointer for the caller. </p>
</dd>

### -param <i>ServerPort</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives an opaque port handle for the communication server port. The minifilter driver uses this handle to listen for incoming connection requests from a user-mode application. </p>
</dd>

### -param <i>ObjectAttributes</i> [in]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a> structure that specifies the attributes of the communication server port. This structure must have been initialized by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a>. This parameter is required and cannot be <b>NULL</b>. Members of this structure for a communication port object include the following. </p>
<table>
<tr>
<th>Member</th>
<th>Value</th>
</tr>
<tr>
<td>
<p><b>ULONG </b><b>Length</b></p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> sets this member to <b>sizeof(</b>OBJECT_ATTRIBUTES<b>)</b>.</p>
</td>
</tr>
<tr>
<td>
<p><b>PUNICODE_STRING </b><b>ObjectName</b></p>
</td>
<td>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure containing a unique name (for example, L"\\MyFilterPort") for the port object. </p>
</td>
</tr>
<tr>
<td>
<p><b>PSECURITY_DESCRIPTOR </b><b>SecurityDescriptor</b></p>
</td>
<td>
<p>Pointer to a security descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>) to be applied to the port object. If needed, a default security descriptor can be created by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541778">FltBuildDefaultSecurityDescriptor</a>. </p>
</td>
</tr>
<tr>
<td>
<p><b>ULONG </b><b>Attributes</b></p>
</td>
<td>
<p>Bitmask of flags specifying the desired attributes for the port handle. These flags must include OBJ_KERNEL_HANDLE. The caller can also optionally set the OBJ_CASE_INSENSITIVE flag, which indicates that name-lookup code should ignore the case of <b>ObjectName</b> rather than performing an exact-match search. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>ServerPortCookie</i> [in, optional]

<dd>
<p>Pointer to context information defined by the minifilter driver. This information can be used to distinguish among multiple communication server ports that are created by the same minifilter driver. The Filter Manager passes this context pointer as a parameter to the <i>ConnectNotifyCallback</i> routine. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param <i>ConnectNotifyCallback</i> [in]

<dd>
<p>Pointer to a caller-supplied callback routine. The Filter Manager calls this routine whenever a user-mode application calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff540460">FilterConnectCommunicationPort</a> to send a connection request to the minifilter driver. This parameter is required and cannot be <b>NULL</b>. This routine is called at IRQL = PASSIVE_LEVEL. </p>
<p>This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef NTSTATUS
(*PFLT_CONNECT_NOTIFY) (
      IN PFLT_PORT ClientPort,
      IN PVOID ServerPortCookie,
      IN PVOID ConnectionContext,
      IN ULONG SizeOfContext,
      OUT PVOID *ConnectionPortCookie
      );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param <a id="ClientPort"></a><a id="clientport"></a><a id="CLIENTPORT"></a><i>ClientPort</i>

<dd>
<p>Opaque handle for the new client port that is established between the user-mode application and the kernel-mode minifilter driver. </p>
<p>The minifilter driver must pass this handle as the <i>ClientPort</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544378">FltSendMessage</a> when sending and replying to messages on this client port. (Note that this is not the same as the <i>ServerPort</i> handle returned by <b>FltCreateCommunicationPort</b>.) </p>
<p>The minifilter driver must eventually close this client port. The client port is closed by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541867">FltCloseClientPort</a>, usually from the minifilter driver's <i>DisconnectNotifyCallback</i> routine. </p>
</dd>

### -param <a id="ServerPortCookie"></a><a id="serverportcookie"></a><a id="SERVERPORTCOOKIE"></a><i>ServerPortCookie</i>

<dd>
<p>Pointer to context information defined by the minifilter driver. This information can be used to distinguish among multiple communication server ports that are created by the same minifilter driver. When the server port was created, the minifilter driver passed this context pointer as a parameter to <b>FltCreateCommunicationPort</b>. </p>
</dd>

### -param <a id="ConnectionContext"></a><a id="connectioncontext"></a><a id="CONNECTIONCONTEXT"></a><i>ConnectionContext</i>

<dd>
<p>Context information pointer that the user-mode application passed in the <i>lpContext</i> parameter to <b>FilterConnectCommunicationPort</b>. </p>
</dd>

### -param <a id="SizeOfContext"></a><a id="sizeofcontext"></a><a id="SIZEOFCONTEXT"></a><i>SizeOfContext</i>

<dd>
<p>Size, in bytes, of the buffer that <i>ConnectionContext </i>points to. </p>
</dd>

### -param <a id="ConnectionPortCookie"></a><a id="connectionportcookie"></a><a id="CONNECTIONPORTCOOKIE"></a><i>ConnectionPortCookie</i>

<dd>
<p>Pointer to information that uniquely identifies this client port. This information is defined by the minifilter driver. The Filter Manager passes this context pointer as a parameter to the minifilter driver's <i>DisconnectNotifyCallback</i> and <i>MessageNotifyCallback</i> routines. </p>
</dd>
</dl>
</dd>

### -param <i>DisconnectNotifyCallback</i> [in]

<dd>
<p>Pointer to a caller-supplied callback routine to be called whenever the user-mode handle count for the client port reaches zero or when the minifilter driver is about to be unloaded. This parameter is required and cannot be <b>NULL</b>. This routine is called at IRQL = PASSIVE_LEVEL. </p>
<p>This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef VOID
(*PFLT_DISCONNECT_NOTIFY) (
      IN PVOID ConnectionCookie
      );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param <a id="ConnectionCookie"></a><a id="connectioncookie"></a><a id="CONNECTIONCOOKIE"></a><i>ConnectionCookie</i>

<dd>
<p>Pointer to information that uniquely identifies this client port. This information is defined by the minifilter driver. When the client port was created, the minifilter driver returned this context pointer in the <i>ConnectionPortCookie</i> parameter of its <i>ConnectNotifyCallback</i> routine. </p>
</dd>
</dl>
</dd>

### -param <i>MessageNotifyCallback</i> [in, optional]

<dd>
<p>Pointer to a caller-supplied callback routine. The Filter Manager calls this routine, at IRQL = PASSIVE_LEVEL, whenever a user-mode application calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff541513">FilterSendMessage</a> to send a message to the minifilter driver through the client port. This parameter is optional and can be <b>NULL</b>. If it is <b>NULL</b>, any request made from user mode to send data to the port will receive an error. </p>
<p>This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef NTSTATUS
(*PFLT_MESSAGE_NOTIFY) (
      IN PVOID PortCookie,
      IN PVOID InputBuffer OPTIONAL,
      IN ULONG InputBufferLength,
      OUT PVOID OutputBuffer OPTIONAL,
      IN ULONG OutputBufferLength,
      OUT PULONG ReturnOutputBufferLength
      );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param <a id="PortCookie"></a><a id="portcookie"></a><a id="PORTCOOKIE"></a><i>PortCookie</i>

<dd>
<p>Pointer to information that uniquely identifies this client port. This information is defined by the minifilter driver. When the client port was created, the minifilter driver returned this context pointer in the <i>ConnectionPortCookie</i> parameter of its <i>ConnectNotifyCallback</i> routine. </p>
</dd>

### -param <a id="InputBuffer"></a><a id="inputbuffer"></a><a id="INPUTBUFFER"></a><i>InputBuffer</i>

<dd>
<p>Pointer to a caller-allocated buffer containing the message to be sent to the minifilter driver. </p>
<p>Note that <i>InputBuffer</i> is a pointer to a raw, unlocked user-mode buffer. This pointer is valid only in the context of the user-mode process and must only be accessed from within a <b>try</b>/<b>except</b> block. </p>
<p>The filter manager calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559876">ProbeForRead</a> to validate this pointer, but it does not ensure that the buffer is properly aligned. If the buffer contains structures that have alignment requirements, the minifilter driver is responsible for performing any necessary alignment checks. To do this, the minifilter driver can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549486">IS_ALIGNED</a> macro as shown in the MiniSpy sample minifilter driver. </p>
<p>This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param <a id="InputBufferLength"></a><a id="inputbufferlength"></a><a id="INPUTBUFFERLENGTH"></a><i>InputBufferLength</i>

<dd>
<p>Size, in bytes, of the buffer that <i>InputBuffer </i>points to. This parameter is ignored if <i>InputBuffer</i> is <b>NULL</b>. </p>
</dd>

### -param <a id="OutputBuffer"></a><a id="outputbuffer"></a><a id="OUTPUTBUFFER"></a><i>OutputBuffer</i>

<dd>
<p>Pointer to a caller-allocated buffer that receives the reply (if any) from the minifilter driver. </p>
<p>Note that <i>OutputBuffer</i> is a pointer to a raw, unlocked user-mode buffer. This pointer is valid only in the context of the user-mode process and must only be accessed from within a <b>try</b>/<b>except</b> block. </p>
<p>The filter manager calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559879">ProbeForWrite</a> to validate this pointer, but it does not ensure that the buffer is properly aligned. If the buffer contains structures that have alignment requirements, the minifilter driver is responsible for performing any necessary alignment checks. To do this, the minifilter driver can use the <b>IS_ALIGNED</b> macro as shown in the MiniSpy sample minifilter driver.</p>
<p>This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param <a id="OutputBufferLength"></a><a id="outputbufferlength"></a><a id="OUTPUTBUFFERLENGTH"></a><i>OutputBufferLength</i>

<dd>
<p>Size, in bytes, of the buffer that <i>OutputBuffer </i>points to. This parameter is ignored if <i>OutputBuffer</i> is <b>NULL</b>. </p>
</dd>

### -param <a id="ReturnOutputBufferLength"></a><a id="returnoutputbufferlength"></a><a id="RETURNOUTPUTBUFFERLENGTH"></a><i>ReturnOutputBufferLength</i>

<dd>
<p>Pointer to a caller-allocated variable that receives the number of bytes returned in the buffer that <i>OutputBuffer</i> points to. </p>
</dd>
</dl>
</dd>

### -param <i>MaxConnections</i> [in]

<dd>
<p>Maximum number of simultaneous client connections to be allowed for this server port. This parameter is required and must be greater than zero. </p>
</dd>
</dl>

## -returns
<p><b>FltCreateCommunicationPort</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The specified <i>Filter</i> is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltCreateCommunicationPort</b> encountered a pool allocation failure. This is an error code. </p><dl>
<dt><b>STATUS_OBJECT_NAME_COLLISION</b></dt>
</dl><p>A minifilter driver communication port with the same name already exists. Port names must be unique. This is an error code. </p>

<p> </p>

## -remarks
<p>A minifilter driver calls <b>FltCreateCommunicationPort</b> to create a communication server port object. </p>

<p>After the server port has been created, a user-mode application can connect to the port by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff540460">FilterConnectCommunicationPort</a>. When connected, the user-mode application can send and receive messages by calling user-mode messaging functions such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff541513">FilterSendMessage</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff540506">FilterGetMessage</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff541508">FilterReplyMessage</a>. </p>

<p>Callers must set the OBJ_KERNEL_HANDLE <b>Attributes</b> flag for the <i>ObjectAttributes</i> parameter of <b>FltCreateCommunicationPort</b>. Setting this flag prevents the minifilter driver communication server port handle from being used by a user-mode process in whose context a caller of <b>FltCreateCommunicationPort</b> might be running. If this flag is not set, <b>FltCreateCommunicationPort</b> returns STATUS_INVALID_PARAMETER. </p>

<p>Any server port that is created by <b>FltCreateCommunicationPort</b> must eventually be closed by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541871">FltCloseCommunicationPort</a>. When the server port is closed, no new connections to the server port are allowed, and all calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff540460">FilterConnectCommunicationPort</a> fail. However, any existing connections remain open until they are closed by the user-mode application or the minifilter driver, or until the minifilter driver is unloaded. </p>

<p>A minifilter driver calls <b>FltCreateCommunicationPort</b> to create a communication server port object. </p>

<p>After the server port has been created, a user-mode application can connect to the port by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff540460">FilterConnectCommunicationPort</a>. When connected, the user-mode application can send and receive messages by calling user-mode messaging functions such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff541513">FilterSendMessage</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff540506">FilterGetMessage</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff541508">FilterReplyMessage</a>. </p>

<p>Callers must set the OBJ_KERNEL_HANDLE <b>Attributes</b> flag for the <i>ObjectAttributes</i> parameter of <b>FltCreateCommunicationPort</b>. Setting this flag prevents the minifilter driver communication server port handle from being used by a user-mode process in whose context a caller of <b>FltCreateCommunicationPort</b> might be running. If this flag is not set, <b>FltCreateCommunicationPort</b> returns STATUS_INVALID_PARAMETER. </p>

<p>Any server port that is created by <b>FltCreateCommunicationPort</b> must eventually be closed by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541871">FltCloseCommunicationPort</a>. When the server port is closed, no new connections to the server port are allowed, and all calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff540460">FilterConnectCommunicationPort</a> fail. However, any existing connections remain open until they are closed by the user-mode application or the minifilter driver, or until the minifilter driver is unloaded. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540460">FilterConnectCommunicationPort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540506">FilterGetMessage</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541513">FilterSendMessage</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541508">FilterReplyMessage</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541778">FltBuildDefaultSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541867">FltCloseClientPort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541871">FltCloseCommunicationPort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542984">FltFreeSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544378">FltSendMessage</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551085">PFLT_FILTER_UNLOAD_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559876">ProbeForRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559879">ProbeForWrite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCreateCommunicationPort function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
