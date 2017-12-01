---
UID: NC.bthddi.PFNBTHPORT_INDICATION_CALLBACK
title: PFNBTHPORT_INDICATION_CALLBACK
author: windows-driver-content
description: Profile drivers implement a L2CAP callback function to provide the Bluetooth driver stack with a mechanism to notify the profile driver about incoming L2CAP connection requests from remote devices, and any changes to the status of a currently open L2CAP connection.
old-location: bltooth\l2cap_callback_function.htm
old-project: bltooth
ms.assetid: d3ca900d-1dd6-49da-ae94-855de3fbd086
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Desktop
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BluetoothPortIndicationCallback
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
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
req.iface: IBidiSpl2
---

# PFNBTHPORT_INDICATION_CALLBACK callback



## -description
<p>Profile drivers implement a L2CAP callback function to provide the Bluetooth driver stack with a
  mechanism to notify the profile driver about incoming L2CAP connection requests from remote devices, and
  any changes to the status of a currently open L2CAP connection.</p>


## -prototype

````
PFNBTHPORT_INDICATION_CALLBACK BluetoothPortIndicationCallback;

void BluetoothPortIndicationCallback(
  _In_ PVOID                  Context,
  _In_ INDICATION_CODE        Indication,
  _In_ PINDICATION_PARAMETERS Parameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>For incoming remote connection request indications, this is the context specified by the profile
     driver in the 
     <b>IndicationCallbackContext</b> member of the 
     <a href="bltooth._brb_l2ca_register_server">
     _BRB_L2CA_REGISTER_SERVER</a> structure when the profile driver registered the callback function. For
     changes to existing L2CAP connections, this is the 
     <b>CallbackContext</b> member specified by the profile driver when it built and sent a 
     <a href="bltooth._brb_l2ca_open_channel">_BRB_L2CA_OPEN_CHANNEL</a> BRB.</p>
</dd>

### -param <i>Indication</i> [in]

<dd>
<p>An 
     <a href="..\bthddi\ne-bthddi--indication-code.md">INDICATION_CODE</a> value that indicates the type
     of L2CAP event.</p>
</dd>

### -param <i>Parameters</i> [in]

<dd>
<p>An 
     <a href="..\bthddi\ns-bthddi--indication-parameters.md">INDICATION_PARAMETERS</a> structure that
     contains event-specific parameters.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A profile driver registers its L2CAP callback function in the following two scenarios:</p>

<p>When a profile driver acts as a server, it registers a L2CAP callback function using the 
      <b>IndicationCallback</b> member of the 
      <a href="bltooth._brb_l2ca_register_server">
      _BRB_L2CA_REGISTER_SERVER</a> structure. The Bluetooth driver stack can then notify the profile
      driver when a remote device attempts to contact it.</p>

<p>When the profile driver acts as a client and attempts to connect to a remote device using the
      <b>BRB_L2CA_OPEN_CHANNEL</b> BRB, the profile driver registers its L2CAP callback function using the 
      <b>Callback</b> member of the _BRB_L2CA_OPEN_CHANNEL structure that is passed when the profile driver 
      <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">builds and sends</a> a 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff536615">BRB_L2CA_OPEN_CHANNEL</a> or 
      <a href="bltooth.brb_l2ca_open_channel_response">
      BRB_L2CA_OPEN_CHANNEL_RESPONSE</a> request.</p>

<p>After the profile driver registers its L2CAP callback function, the callback function is only
    associated with the channel that the BRB opened. The Bluetooth driver stack can call the L2CAP callback
    function to notify the profile driver of actions that occur over the open channel to the remote device.
    Profile drivers can register a single callback function to handle channel notifications as a client and
    connection notifications as a server.</p>

<p>The 
    <a href="..\bthddi\ns-bthddi--indication-parameters.md">INDICATION_PARAMETERS</a> structure held in
    the 
    <i>Parameters</i> parameter is interpreted according to the value of the 
    <a href="..\bthddi\ne-bthddi--indication-code.md">INDICATION_CODE</a> enumeration that the Bluetooth
    driver stack passes to the profile driver's L2CAP callback function through the 
    <i>Indication</i> parameter. For most notifications, there is an INDICATION_PARAMETERS union member that
    corresponds to the event and contains event-specific parameters.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback
   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access
   paged memory)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="bltooth._brb_l2ca_register_server">_BRB_L2CA_REGISTER_SERVER</a>
</dt>
<dt>
<a href="bltooth._brb_l2ca_open_channel">_BRB_L2CA_OPEN_CHANNEL</a>
</dt>
<dt>
<a href="..\bthddi\ne-bthddi--indication-code.md">INDICATION_CODE</a>
</dt>
<dt>
<a href="..\bthddi\ns-bthddi--indication-parameters.md">INDICATION_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20PFNBTHPORT_INDICATION_CALLBACK callback function%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
