---
UID: NE.bthddi._INDICATION_CODE
title: INDICATION_CODE
author: windows-driver-content
description: The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has occurred.
old-location: bltooth\indication_code.htm
old-project: bltooth
ms.assetid: 7fc374e3-ca5b-476d-bc44-afb28ecf9920
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INDICATION_CODE
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

# INDICATION_CODE enumeration



## -description
<p>The INDICATION_CODE enumeration type indicates to a profile driver what type of L2CAP event has
  occurred.</p>


## -syntax

````
typedef enum _INDICATION_CODE { 
  IndicationAddReference          = 0,
  IndicationReleaseReference,
  IndicationRemoteConnect,
  IndicationRemoteDisconnect,
  IndicationRemoteConfigRequest   = 4,
  IndicationRemoteConfigResponse,
  IndicationFreeExtraOptions      = 6,
  IndicationRecvPacket,
  IndicationPairDevice,
  IndicationUnpairDevice          = 9,
  IndicationUnpersonalizeDevice,
  IndicationRemoteConnectLE
} INDICATION_CODE, *PINDICATION_CODE;
````


## -enum-fields
<dl>

### -field IndicationAddReference

<dd>
<p>Indicates to a profile driver to add a reference to its device object because it may be called at
     any time.</p>
</dd>

### -field IndicationReleaseReference

<dd>
<p>Indicates to a profile driver to release a reference to its device object and that it will no
     longer be called.</p>
</dd>

### -field IndicationRemoteConnect

<dd>
<p>Indicates to a server profile driver that a remote device is connecting to the PSM that the
     profile driver registered earlier. Profile drivers accept or reject this request by 
     <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">building and sending</a> a 
     <a href="bltooth.brb_l2ca_open_channel_response">
     BRB_L2CA_OPEN_CHANNEL_RESPONSE</a> request. When this indication code is passed, the profile driver
     should use the parameters that are passed to it in the 
     <b>Connect</b> member of the 
     <a href="..\bthddi\ns-bthddi--indication-parameters.md">
     INDICATION_PARAMETERS</a> structure.</p>
</dd>

### -field IndicationRemoteDisconnect

<dd>
<p>Indicates to a registered profile driver that a remote device disconnecting from the local radio.
     When this indication code is passed, the profile driver should use the parameters that are passed to it
     in the 
     <b>Disconnect</b> member of the INDICATION_PARAMETERS structure.</p>
</dd>

### -field IndicationRemoteConfigRequest

<dd>
<p>Indicates to a client profile driver that a remote device is performing a configuration request.
     When this indication code is passed, the profile driver should use the parameters that are passed to it
     in the 
     <b>ConfigRequest</b> member of the INDICATION_PARAMETERS structure.</p>
</dd>

### -field IndicationRemoteConfigResponse

<dd>
<p>Indicates to a client profile driver that a remote device is responding to a configuration
     request. When this indication code is passed, the profile driver should use the parameters that are
     passed to it in the 
     <b>ConfigResponse</b> member of the INDICATION_PARAMETERS structure.</p>
</dd>

### -field IndicationFreeExtraOptions

<dd>
<p>Reserved for future use. Do not use.</p>
</dd>

### -field IndicationRecvPacket

<dd>
<p>Indicates to a registered profile driver that a packet has been received on the specified PSM. The
     profile driver can use this event to determine when it is necessary to issue a read
     BRB_L2CA_ACL_TRANSFTER BRB. Profile drivers that need to read from the remote device can also ignore
     this notification and keep a read BRB pending at all times. When this indication code is passed, the
     profile driver should use the parameters that are passed to it in the 
     <b>RecvPacket</b> member of the 
     <a href="..\bthddi\ns-bthddi--indication-parameters.md">
     INDICATION_PARAMETERS</a> structure.</p>
</dd>

### -field IndicationPairDevice

<dd>
<p>Indicates to a registered driver that the local radio has bonded to a specific remote
     radio.</p>
</dd>

### -field IndicationUnpairDevice

<dd>
<p>Indicates to a registered driver that the local radio is no longer bonded to a specific remote
     radio.</p>
</dd>

### -field IndicationUnpersonalizeDevice

<dd>
<p>Indicates to a registered driver that the specified remote radio has been removed from the list of
     personal devices.</p>
</dd>

### -field IndicationRemoteConnectLE

<dd>
<p>Indicates to a server profile driver that a low energy (LE) remote device is connecting to the PSM that the
     profile driver registered earlier. Profile drivers accept or reject this request by 
     <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">building and sending</a> a 
     <a href="bltooth.brb_l2ca_open_channel_response">
     BRB_L2CA_OPEN_CHANNEL_RESPONSE</a> request. When this indication code is passed, the profile driver
     should use the parameters that are passed to it in the 
     <b>Connect</b> member of the 
     <a href="..\bthddi\ns-bthddi--indication-parameters.md">
     INDICATION_PARAMETERS</a> structure. This value is present in Windows 8 and later versions of Windows.</p>
</dd>
</dl>

## -remarks
<p>A value from this enumeration is passed to a profile driver's 
    <a href="..\bthddi\nc-bthddi-pfnbthport-indication-callback.md">L2CAP Callback Function</a> to notify
    it of an event.</p>

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
<a href="..\bthioctl\ni-bthioctl-ioctl-internal-bth-submit-brb.md">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>
</dt>
<dt>
<a href="..\bthddi\ns-bthddi--indication-parameters.md">INDICATION_PARAMETERS</a>
</dt>
<dt>
<a href="..\bthddi\nc-bthddi-pfnbthport-indication-callback.md">L2CAP Callback Function</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536618">BRB_L2CA_REGISTER_SERVER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20INDICATION_CODE enumeration%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
