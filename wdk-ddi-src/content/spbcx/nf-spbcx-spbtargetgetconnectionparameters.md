---
UID: NF.spbcx.SpbTargetGetConnectionParameters
title: SpbTargetGetConnectionParameters
author: windows-driver-content
description: The SpbTargetGetConnectionParameters method retrieves the connection parameters for a target device on the bus.
old-location: spb\spbtargetgetconnectionparameters.htm
old-project: SPB
ms.assetid: 0692D8A3-CA43-4D27-9E8E-EB104DB1651F
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SpbTargetGetConnectionParameters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: spbcx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpbTargetGetConnectionParameters
req.alt-loc: spbcxstubs.lib,spbcxstubs.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spbcxstubs.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# SpbTargetGetConnectionParameters function



## -description
<p>The <b>SpbTargetGetConnectionParameters</b> method retrieves the connection parameters for a target device on the bus.</p>


## -syntax

````
VOID SpbTargetGetConnectionParameters(
  _In_  SPBTARGET                 Target,
  _Out_ SPB_CONNECTION_PARAMETERS *ConnectionParameters
);
````


## -parameters
<dl>

### -param <i>Target</i> [in]

<dd>
<p>An <a href="buses.spbtarget_object_handle">SPBTARGET</a> handle to the target device for which to retrieve the connection parameters.</p>
</dd>

### -param <i>ConnectionParameters</i> [out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/hh406204">SPB_CONNECTION_PARAMETERS</a> structure into which the method writes the connection parameters. The caller must previously have called the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406205">SPB_CONNECTION_PARAMETERS_INIT</a> function to initialize this structure.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>This method retrieves a set of connection parameters that the SPB controller driver requires to access the specified target device on the bus. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406204">SPB_CONNECTION_PARAMETERS</a>.</p>

<p>A client (peripheral driver) that successfully opens a connection to a target has exclusive use of that target.</p>

<p>The SPB framework extension (SpbCx) calls your controller driver's <a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a> and <a href="https://msdn.microsoft.com/02756C35-E76C-42C0-80FA-359CADE224A1">EvtSpbTargetDisconnect</a> callback functions to open and close a connection.</p>

<p><b>SpbTargetGetConnectionParameters</b> will not fail if it is called with a valid SPBTARGET handle.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Spbcx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spbcxstubs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/02756C35-E76C-42C0-80FA-359CADE224A1">EvtSpbTargetDisconnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406204">SPB_CONNECTION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406205">SPB_CONNECTION_PARAMETERS_INIT</a>
</dt>
<dt>
<a href="buses.spbtarget_object_handle">SPBTARGET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SpbTargetGetConnectionParameters method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
