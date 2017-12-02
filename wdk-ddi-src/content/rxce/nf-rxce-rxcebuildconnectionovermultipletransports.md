---
UID: NF.rxce.RxCeBuildConnectionOverMultipleTransports
title: RxCeBuildConnectionOverMultipleTransports
author: windows-driver-content
description: RxCeBuildConnectionOverMultipleTransports establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports.
old-location: ifsk\rxcebuildconnectionovermultipletransports.htm
old-project: ifsk
ms.assetid: 9ef9a5a5-e0ad-46c0-8193-8d2a18a21ea0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxCeBuildConnectionOverMultipleTransports
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxce.h
req.include-header: Rxce.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCeBuildConnectionOverMultipleTransports
req.alt-loc: rxce.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RxCeBuildConnectionOverMultipleTransports function



## -description
<p><b>RxCeBuildConnectionOverMultipleTransports</b> establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. A set of local addresses are specified and this routine attempts to connect to the target server via all the transports associated with the local addresses. One connection is chosen as the winner depending on the connect options.</p>


## -syntax

````
NTSTATUS RxCeBuildConnectionOverMultipleTransports(
  _Inout_ PRDBSS_DEVICE_OBJECT                pMiniRedirectorDeviceObject,
  _In_    RXCE_CONNECTION_CREATE_OPTIONS      CreateOptions,
  _In_    ULONG                               NumberOfAddresses,
  _In_    PRXCE_ADDRESS                       *pLocalAddressPointers,
  _In_    PUNICODE_STRING                     pServerName,
  _In_    PRXCE_CONNECTION_INFORMATION        pConnectionInformation,
  _In_    PRXCE_CONNECTION_EVENT_HANDLER      pHandler,
  _In_    PVOID                               pEventContext,
  _In_    PRXCE_CONNECTION_COMPLETION_ROUTINE pCompletionRoutine,
  _Inout_ PRXCE_CONNECTION_COMPLETION_CONTEXT pCompletionContext
);
````


## -parameters
<dl>

### -param pMiniRedirectorDeviceObject [in, out]

<dd>
<p>A pointer to the mini-redirector device object.</p>
</dd>

### -param CreateOptions [in]

<dd>
<p>Create options that determine which transport will be selected for establishing a connection. These options can be one of the following enumerations for RXCE_CONNECTION_CREATE_OPTIONS:</p>
<p></p>
<dl>

### -param RxCeSelectFirstSuccessfulTransport

<dd>
<p>Select the first successful transport that responds.</p>
</dd>

### -param RxCeSelectBestSuccessfulTransport

<dd>
<p>Select the best successful transport that responds.</p>
</dd>

### -param RxCeSelectAllSuccessfulTransports

<dd>
<p>Select all of the successful transports that respond.</p>
</dd>
</dl>
</dd>

### -param NumberOfAddresses [in]

<dd>
<p>The number of local addresses (transports).</p>
</dd>

### -param pLocalAddressPointers [in]

<dd>
<p>A pointer to an array of the local address handles.</p>
</dd>

### -param pServerName [in]

<dd>
<p>A pointer to the name of the server (for connection enumeration).</p>
</dd>

### -param pConnectionInformation [in]

<dd>
<p>A pointer to the connection information that specifies the remote address.</p>
</dd>

### -param pHandler [in]

<dd>
<p>A pointer to the event handler for processing receive indications.</p>
</dd>

### -param pEventContext [in]

<dd>
<p>A pointer to the context parameter to be passed back to the event handler and used for indications.</p>
</dd>

### -param pCompletionRoutine [in]

<dd>
<p>A pointer to a connection completion routine when this routine completed if STATUS_PENDING is initially returned.</p>
</dd>

### -param pCompletionContext [in, out]

<dd>
<p>On input, this parameter contains a pointer to an uninitialized RXCE_CONNECTION_COMPLETION_CONTEXT structure. On output when this call is successful, the virtual circuit is associated with the connection and the virtual circuit and connection are properly initialized.</p>
</dd>
</dl>

## -returns
<p><b>RxCeBuildConnectionOverMultipleTransports</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of nonpaged pool memory needed by this routine failed. </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>It was not possible to initialize a connection and a virtual circuit with any of the multiple transports. This error can occur if all of the RDBSS transports or the RBDSS connection engine addresses pointed to in the <i>pLocalAddressPointers</i> array are invalid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters passed to this routine was invalid. </p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>One of the asynchronous calls to the different transports passed as input parameters to the routine is still outstanding and has not been completed. </p>

<p> </p>

## -remarks
<p><b>RxCeBuildConnectionOverMultipleTransports</b> will initiate a series of asynchronous calls to all of the different transports passed in as parameters to try and build a connection. The network mini-redirector cannot be unloaded until all of these asynchronous requests are completed.</p>

<p><b>RxCeBuildConnectionOverMultipleTransports</b> must be called in the context of a system worker thread.</p>

<p>When <b>RxCeBuildConnectionOverMultipleTransports</b> is successful, the virtual circuit will be properly initialized and connections will be established.</p>

<p><b>RXCE_CONNECTION_INFORMATION</b> is a typedef for a <b>TDI_CONNECTION_INFORMATION</b> structure. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxce.h (include Rxce.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\rxce\nf-rxce-rxcebuildconnection.md">RxCeBuildConnection</a>
</dt>
<dt>
<a href="..\rxce\nf-rxce-rxceteardownconnection.md">RxCeTearDownConnection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565085">TDI_CONNECTION_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeBuildConnectionOverMultipleTransports routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
