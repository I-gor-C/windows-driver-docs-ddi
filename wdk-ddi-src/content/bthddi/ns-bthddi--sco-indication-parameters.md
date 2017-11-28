---
UID: NS.bthddi._SCO_INDICATION_PARAMETERS
title: SCO_INDICATION_PARAMETERS
author: windows-driver-content
description: The SCO_INDICATION_PARAMETERS structure describes indication parameters about a SCO connect or disconnect notification.
old-location: bltooth\sco_indication_parameters.htm
old-project: bltooth
ms.assetid: 2d3ae219-8a40-476c-b8eb-94f4c0566527
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SCO_INDICATION_PARAMETERS, SCO_INDICATION_PARAMETERS, *PSCO_INDICATION_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCO_INDICATION_PARAMETERS
req.alt-loc: bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback
   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access
   paged memory)
req.iface: IBidiSpl2
---

# SCO_INDICATION_PARAMETERS structure



## -description
<p>The SCO_INDICATION_PARAMETERS structure describes indication parameters about a SCO connect or
  disconnect notification.</p>


## -syntax

````
typedef struct _SCO_INDICATION_PARAMETERS {
  SCO_CHANNEL_HANDLE ConnectionHandle;
  BTH_ADDR           BtAddress;
  union {
    struct {
      struct {
        SCO_LINK_TYPE LinkType;
      } Request;
    } Connect;
    struct {
      SCO_DISCONNECT_REASON Reason;
      BOOLEAN               CloseNow;
    } Disconnect;
  } Parameters;
} SCO_INDICATION_PARAMETERS, *PSCO_INDICATION_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>ConnectionHandle</b>

<dd>
<p>A connection handle to the remote device. This handle is only valid for notifications that arrive
     over an established SCO connection.</p>
</dd>

### -field <b>BtAddress</b>

<dd>
<p>The Bluetooth address of the remote device.</p>
</dd>

### -field <b>Parameters</b>

<dd>
<dl>


</dl>
<dl>

### -field <b>Connect</b>

<dd>
<p>The structure that contains parameters for the 
      <b>ScoIndicationRemoteConnectSCO_INDICATION_CODE</b> event.</p>
<dl>

### -field <b>Request</b>

<dd>
<p>The structure that contains the parameters for the SCO connection request.</p>
<dl>

### -field <b>LinkType</b>

<dd>
<p>A value from the 
        <a href="https://msdn.microsoft.com/library/windows/hardware/ff536781">SCO_LINK_TYPE</a> enumeration that indicates the
        type of incoming connection.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>Disconnect</b>

<dd>
<p>The structure that contains parameters for the 
      <b>ScoIndicationRemoteDisconnectSCO_INDICATION_CODE</b> event.</p>
<dl>

### -field <b>Reason</b>

<dd>
<p>A 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff536775">SCO_DISCONNECT_REASON</a> value that
       indicates why the SCO connection was terminated.</p>
</dd>

### -field <b>CloseNow</b>

<dd>
<p>A Boolean value that a profile driver can set to indicate whether the SCO connection to the
       remote device will be closed. If the connection is to be closed, the value is <b>TRUE</b>. Otherwise, the
       value is <b>FALSE</b>.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>A profile driver's 
    <a href="..\bthddi\nc-bthddi-pfnsco-indication-callback.md">SCO Callback Function</a> should process
    a notification differently depending upon the value that the Bluetooth driver stack passes in the 
    <i>Indication</i> parameter of the callback function.</p>

<p>When the Bluetooth driver stack passes 
    <b>ScoIndicationRemoteConnect</b>, the callback function should use the 
    <b>Connect</b> member of the 
    <b>Parameters</b> union.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthddi.h (include Bthddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536775">SCO_DISCONNECT_REASON</a>
</dt>
<dt>
<a href="..\bthddi\nc-bthddi-pfnsco-indication-callback.md">SCO Callback Function</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20SCO_INDICATION_PARAMETERS structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
