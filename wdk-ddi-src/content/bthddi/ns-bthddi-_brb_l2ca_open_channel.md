---
UID : NS:bthddi._BRB_L2CA_OPEN_CHANNEL
title : _BRB_L2CA_OPEN_CHANNEL
author : windows-driver-content
description : The _BRB_L2CA_OPEN_CHANNEL structure describes a L2CAP channel to open to a remote device, or a response from the profile driver accepting or rejecting an incoming L2CAP connection request that was initiated by a remote device.
old-location : bltooth\_brb_l2ca_open_channel.htm
old-project : bltooth
ms.assetid : 16f79360-c8fd-4be9-9c94-7fa2a1d8c6b5
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : _BRB_L2CA_OPEN_CHANNEL, bth_structs_342ad84f-74fb-481f-b549-8f87c375c4d1.xml, _BRB_L2CA_OPEN_CHANNEL structure [Bluetooth Devices], bthddi/_BRB_L2CA_OPEN_CHANNEL, bltooth._brb_l2ca_open_channel
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bthddi.h
req.include-header : Bthddi.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows Vista, and later.
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
req.irql : Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---

# _BRB_L2CA_OPEN_CHANNEL structure
The _BRB_L2CA_OPEN_CHANNEL structure describes a L2CAP channel to open to a remote device, or a
  response from the profile driver accepting or rejecting an incoming L2CAP connection request that was
  initiated by a remote device.

## Syntax
````
struct _BRB_L2CA_OPEN_CHANNEL {
  BRB_HEADER                     Hdr;
  L2CAP_CHANNEL_HANDLE           ChannelHandle;
  union {
    struct {
      USHORT Response;
      USHORT ResponseStatus;
    };
    USHORT Psm;
  };
  ULONG                          ChannelFlags;
  BTH_ADDR                       BtAddress;
  struct {
    ULONG                    Flags;
    L2CAP_CONFIG_VALUE_RANGE Mtu;
    L2CAP_CONFIG_VALUE_RANGE FlushTO;
    L2CAP_FLOWSPEC           Flow;
    USHORT                   LinkTO;
    ULONG                    NumExtraOptions;
    PL2CAP_CONFIG_OPTION     ExtraOptions;
    struct {
      UCHAR ServiceType;
      ULONG Latency;
    } LocalQos;
  } ConfigOut;
  struct {
    ULONG                    Flags;
    L2CAP_CONFIG_VALUE_RANGE Mtu;
    L2CAP_CONFIG_RANGE       FlushTO;
  } ConfigIn;
  ULONG                          CallbackFlags;
  PFNBTHPORT_INDICATION_CALLBACK Callback;
  PVOID                          CallbackContext;
  PVOID                          ReferenceObject;
  CHANNEL_CONFIG_RESULTS         OutResults;
  CHANNEL_CONFIG_RESULTS         InResults;
  UCHAR                          IncomingQueueDepth;
};
````

## Members


`BtAddress`

The Bluetooth address of the device for which the connection is intended.

`Callback`

The 
     <mshelp:link keywords="bltooth.l2cap_callback_function" tabindex="0"><i>L2CAP Callback
     Function</i></mshelp:link> implemented by the profile driver, that the Bluetooth driver stack should call to notify
     the profile driver about any changes to the L2CAP connection.

`CallbackContext`

The context to pass to the callback function specified in the 
     <b>Callback</b> member. The profile driver defines this value.

`CallbackFlags`

A flag that specifies which events should generate a callback routine to notify the profile driver
     that the event has occurred. Valid flag values are contained in the following table.
     
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
CALLBACK_CONFIG_EXTRA_IN

</td>
<td>
If set, the callback routine will be called when the configuration request for the remote device
        contains extra options. If not set, the extra configuration options will be rejected as unknown
        options. This flag is used with <b>BRB_L2CA_OPEN_CHANNEL_RESPONSE</b> BRBs.

</td>
</tr>
<tr>
<td>
CALLBACK_CONFIG_EXTRA_OUT

</td>
<td>
If set, the callback routine will be called when the remote device rejects an extra configuration
        option from a <b>BRB_L2CA_OPEN_CHANNEL</b> request. If not set and the remote device rejects the
        configuration request due to an extra option, the connection will be closed.

</td>
</tr>
<tr>
<td>
CALLBACK_CONFIG_QOS

</td>
<td>
If set, the callback routine will be called when a remote device sends a configuration request
        that contains a QOS value. If this flag is not set and the remote device either sends QOS parameters
        in a configuration request or rejects the profile driver's requested QOS parameters, the connection
        is disconnected.

</td>
</tr>
<tr>
<td>
CALLBACK_DISCONNECT

</td>
<td>
If set, the callback routine will be called when a remote device disconnects from the L2CAP
        channel.

</td>
</tr>
<tr>
<td>
CALLBACK_RECV_PACKET

</td>
<td>
If set, the callback routine will be called when the profile driver receives an incoming L2CAP
        packet.

</td>
</tr>
</table>

`ChannelFlags`

Flags that specify the requirements for the channel to be opened. Valid flag values are listed in
     the following table:
     
<table>
<tr>
<td>
<b>Flag</b>

</td>
<td>
<b>Description</b>

</td>
</tr>
<tr>
<td>
CF_LINK_AUTHENTICATED

</td>
<td>
The link must be authenticated.

</td>
</tr>
<tr>
<td>
CF_LINK_ENCRYPTED

</td>
<td>
The link must be encrypted. Setting this flag also sets the CF_LINK_AUTHENTICATED flag.

</td>
</tr>
<tr>
<td>
CF_LINK_SUPPRESS_PIN

</td>
<td>
The profile driver indicates its preference that users not be prompted for a PIN.

</td>
</tr>
</table>

`ChannelHandle`



`ConfigIn`

The substructure that contains parameter settings to validate incoming
     <b>BRB_L2CA_OPEN_CHANNEL_RESPONSE</b> BRBs that are sent from a remote device.

`ConfigOut`

The substructure that contains parameter settings for a <b>BRB_L2CA_OPEN_CHANNEL</b> BRB sent to a remote
     device.

`Hdr`

A 
     <a href="..\bthddi\ns-bthddi-_brb_header.md">BRB_HEADER</a> structure that contains information
     about the current BRB.

`IncomingQueueDepth`

Specifies the incoming queue length in message transfer units (MTUs).

`InResults`

A CHANNEL_CONFIG_RESULTS structure that contains configuration parameters for the inbound
     request.

`OutResults`

A 
     <a href="..\bthddi\ns-bthddi-_channel_config_results.md">CHANNEL_CONFIG_RESULTS</a> structure that
     contains configuration parameters for the outbound request.

`ReferenceObject`

A pointer to an object to pass to 
     <a href="..\wdm\nf-wdm-obreferenceobject.md">ObReferenceObject</a> and 
     <a href="..\wdm\nf-wdm-obdereferenceobject.md">ObDereferenceObject</a> for which to
     maintain a reference count of.

## Remarks
To open a L2CAP channel, profile drivers should 
    <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">build and send</a> a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff536615">BRB_L2CA_OPEN_CHANNEL</a> request.

Profile drivers that act as clients specify a destination address, a PSM, and a variety of
    configuration parameters.

If the <b>BRB_L2CA_OPEN_CHANNEL</b> request completes successfully, a variety of information about the newly
    created connection is available in the 
    <b>OutResults</b> and 
    <b>InResults</b> members. 
    <b>OutResults</b> specifies the parameters for the outbound half of the channel, and 
    <b>InResults</b> specifies the parameters for the inbound half of the channel.

Several of the configuration parameters passed in this structure, such as the 
    <b>Mtu</b> member, are ranges used for negotiation with the remote radio. Clients should provide as wide a
    range as possible to increase the chances of successful channel negotiation. Specifying a minimum MTU
    size greater than the basic Bluetooth minimum MTU size should only be done when absolutely necessary. If
    negotiation fails, the connection will fail.

Profile drivers must allocate the memory to store the array that is stored in the 
    <b>ExtraOptions</b> member and should not free this memory until the callback function defined in the 
    <b>Callback</b> member returns with an 
    <b>IndicationFreeExtraOptions</b> notification 
    <a href="..\bthddi\ne-bthddi-_indication_code.md">INDICATION_CODE</a> value passed in its 
    <i>Indication</i> parameter.

The 
    <b>IncomingQueueDepth</b> member of the _BRB_L2CA_OPEN_CHANNEL structure specifies the maximum number of
    MTUs that the Bluetooth driver stack will receive and queue on the connection before it begins to discard
    them. Setting this value to a very small number increases the chances of data loss, while setting it to a
    very large number can increase memory usage. Setting this member to 10 is an effective compromise.

To accept or reject an incoming L2CAP connection request initiated by a remote device, profile drivers
    should 
    <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">build and send</a> a 
    <mshelp:link keywords="bltooth.brb_l2ca_open_channel_response" tabindex="0"><b>
    BRB_L2CA_OPEN_CHANNEL_RESPONSE</b></mshelp:link> request.

A profile driver should build and send a <b>BRB_L2CA_OPEN_CHANNEL_RESPONSE</b> request when the Bluetooth
    driver stack calls the profile driver's 
    <a href="..\bthddi\nc-bthddi-pfnbthport_indication_callback.md">L2CAP Callback Function</a> and passes 
    <b>IndicationRemoteConnect</b> in the callback function's 
    <i>Indication</i> parameter.

Based on the value of the 
    <b>Response</b> member of this structure, the Bluetooth driver stack will then accept or reject the
    connection request.

The profile driver specifies whether the connection should be accepted by storing an appropriate value
    in the 
    <b>Response</b> member of this structure.

Upon receiving the CONNECT_RSP_RESULT_PENDING response, the connecting client should reset its
    connection timer and wait for an updated connection response message. Profile drivers calling the
    <b>BRB_L2CA_OPEN_CHANNEL_RESPONSE</b> BRB where the 
    <b>Response</b> member is set to CONNECT_RSP_RESULT_PENDING should promptly issue an additional
    <b>BRB_L2CA_OPEN_CHANNEL_RESPONSE</b> BRB with an updated connection value. The updated value can be any of the
    status codes described in the 
    <b>Response</b> member, including resending a CONNECT_RSP_RESULT_PENDING value.

Profile drivers must allocate the memory to store the array that is stored in the 
    <b>ExtraOptions</b> member and should not free this memory until the callback function that is defined in
    the 
    <b>Callback</b> member returns with an 
    <b>IndicationFreeExtraOptions</b> notification 
    <b>INDICATION_CODE</b> value passed in its 
    <i>Indication</i> parameter.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="..\wdm\nf-wdm-obreferenceobject.md">ObReferenceObject</a>

<a href="..\bthddi\ns-bthddi-_l2cap_config_option.md">L2CAP_CONFIG_OPTION</a>

<mshelp:link keywords="bltooth.brb_l2ca_open_channel_response" tabindex="0"><b>
   BRB_L2CA_OPEN_CHANNEL_RESPONSE</b></mshelp:link>

<a href="..\wdm\nf-wdm-obdereferenceobject.md">ObDereferenceObject</a>

<a href="..\bthddi\ns-bthddi-_brb_header.md">BRB_HEADER</a>

<a href="..\bthddi\nc-bthddi-pfnbthport_indication_callback.md">L2CAP Callback Function</a>

<a href="..\bthddi\ns-bthddi-_channel_config_results.md">CHANNEL_CONFIG_RESULTS</a>

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff536618">BRB_L2CA_REGISTER_SERVER</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536615">BRB_L2CA_OPEN_CHANNEL</a>

<a href="..\bthddi\ns-bthddi-_indication_parameters.md">INDICATION_PARAMETERS</a>

<a href="..\bthddi\ne-bthddi-_indication_code.md">INDICATION_CODE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20_BRB_L2CA_OPEN_CHANNEL structure%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>