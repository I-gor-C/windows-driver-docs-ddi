---
UID: NC.ndis.PROTOCOL_CL_OPEN_AF_COMPLETE_EX
title: PROTOCOL_CL_OPEN_AF_COMPLETE_EX
author: windows-driver-content
description: The ProtocolClOpenAfCompleteEx function completes the opening of an address family (AF) that was started when a CoNDIS client called the NdisClOpenAddressFamilyEx function.Note  You must declare the function by using the PROTOCOL_CL_OPEN_AF_COMPLETE_EX type. For more information, see the following Examples section.
old-location: netvista\protocolclopenafcompleteex.htm
old-project: netvista
ms.assetid: 03ddbbfd-8fe8-44b6-8d3e-12a7bf6f8f6b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClOpenAfCompleteEx
req.alt-loc: Ndis.h
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
---

# PROTOCOL_CL_OPEN_AF_COMPLETE_EX callback



## -description
<p>The 
  <i>ProtocolClOpenAfCompleteEx</i> function completes the opening of an address family (AF) that was started
  when a CoNDIS client called the 
  <a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">NdisClOpenAddressFamilyEx</a> function.</p>


## -prototype

````
PROTOCOL_CL_OPEN_AF_COMPLETE_EX ProtocolClOpenAfCompleteEx;

VOID ProtocolClOpenAfCompleteEx(
  _In_ NDIS_HANDLE ProtocolAfContext,
  _In_ NDIS_HANDLE NdisAfHandle,
  _In_ NDIS_STATUS Status
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProtocolAfContext</i> [in]

<dd>
<p>A client-supplied handle to its context area for an address AF. The client allocated this context
     area and passed this handle to NDIS in its call to the 
     <a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">
     NdisClOpenAddressFamilyEx</a> function.</p>
</dd>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>An NDIS-supplied handle to an AF, if 
     <i>Status</i> is NDIS_STATUS_SUCCESS. Otherwise, this parameter is <b>NULL</b>. This handle represents an
     association that NDIS established between the client and a call manager that is bound to a CoNDIS
     miniport adapter. If the handle is not <b>NULL</b>, the client must save the handle for use in subsequent calls
     to 
     <b>NdisCl<i>Xxx</i></b> and 
     <b>NdisCo<i>Xxx</i></b> functions.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>The final status of the client's call to 
     <b>NdisClOpenAddressFamilyEx</b>, which can be any of the following: 
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The AF has been opened, so the client can initialize its state at 
       <i>ProtocolAfContext</i> and use the returned handle from 
       <i>NdisAfHandle</i> in subsequent calls to 
       <b>NdisCl<i>Xxx</i></b> and 
       <b>NdisCo<i>Xxx</i></b> functions, such as 
       <a href="..\ndis\nf-ndis-ndiscooidrequest.md">NdisCoOidRequest</a>.</p>
</dd>

### -param <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>The requested operation failed because NDIS or the call manager could not allocate sufficient
       memory or initialize the state that one of them uses to track the client's open of the AF that 
       <i>ProtocolAfContext</i> specifies.</p>
</dd>

### -param <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>NDIS failed the call, possibly for one of the following reasons:
       </p>
<ul>
<li>
<p>The given AF does not match any AF that was registered for the underlying miniport driver to
         which the caller is bound.</p>
</li>
<li>
<p>The caller's adapter binding is closing.</p>
</li>
<li>
<p>The call manager that registered the specified AF is closing its binding to the underlying
         miniport adapter.</p>
</li>
</ul>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <i>ProtocolClOpenAfCompleteEx</i> function is required for CoNDIS clients. CoNDIS clients must provide 
    <i>ProtocolClOpenAfCompleteEx</i> to complete the asynchronous operations that the clients initiate by
    calling the 
    <a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">
    NdisClOpenAddressFamilyEx</a> function.</p>

<p>NDIS calls 
    <i>ProtocolClOpenAfCompleteEx</i> to indicate that some or all of the following have occurred:</p>

<p>If all of the parameters that the client's 
      <a href="..\ndis\nc-ndis-protocol-co-af-register-notify.md">
      ProtocolCoAfRegisterNotify</a> function passed to the 
      <b>NdisClOpenAddressFamilyEx</b> function were valid, NDIS called the 
      <a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a> function of the
      call manager that just registered the specified AF with NDIS.</p>

<p>The call manager has examined the specification that the client's 
      <i>ProtocolCoAfRegisterNotify</i> function passed to 
      <b>NdisClOpenAddressFamilyEx</b> at the 
      <i>AddressFamily</i> parameter and returned whether it was valid for this call manager to NDIS.</p>

<p>If the client's attempt to open an AF fails, NDIS cleans up its saved state before calling 
    <i>ProtocolClOpenAfCompleteEx</i>. In this case, 
    <i>ProtocolClOpenAfCompleteEx</i> can release the resources that the client allocated for its call to 
    <a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">NdisClOpenAddressFamilyEx</a> or
    prepare them for reuse.</p>

<p>Otherwise, 
    <i>ProtocolClOpenAfCompleteEx</i> should set up whatever client-determined state the client will need for
    subsequent operations on the newly opened AF. In particular, the client must save the handle from the 
    <i>NdisAfHandle</i> parameter, typically in the client's 
    <i>ProtocolAfContext</i> context area.</p>

<p>If the client accepts incoming calls, it might allocate a per-service access point (SAP) state area
    and call the 
    <a href="..\ndis\nf-ndis-ndisclregistersap.md">NdisClRegisterSap</a> function. If the
    client makes outgoing calls, it might allocate a per-virtual connection (VC) state area and create a VC
    with the 
    <a href="..\ndis\nf-ndis-ndiscocreatevc.md">NdisCoCreateVc</a> function to prepare for an
    incoming request from one of the client's own clients to make an outgoing call to a remote node.</p>

<p>NDIS calls 
    <i>ProtocolClOpenAfCompleteEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>ProtocolClOpenAfCompleteEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClOpenAfCompleteEx</i> function that is named "MyClOpenAfCompleteEx", use the <b>PROTOCOL_CL_OPEN_AF_COMPLETE_EX</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_OPEN_AF_COMPLETE_EX</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_OPEN_AF_COMPLETE_EX</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
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
<a href="..\ndis\nf-ndis-ndisclopenaddressfamilyex.md">NdisClOpenAddressFamilyEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisclregistersap.md">NdisClRegisterSap</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscocreatevc.md">NdisCoCreateVc</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscooidrequest.md">NdisCoOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-af-register-notify.md">ProtocolCoAfRegisterNotify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_OPEN_AF_COMPLETE_EX callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
