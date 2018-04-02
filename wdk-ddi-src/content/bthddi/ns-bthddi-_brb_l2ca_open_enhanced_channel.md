---
UID: NS:bthddi._BRB_L2CA_OPEN_ENHANCED_CHANNEL
title: "_BRB_L2CA_OPEN_ENHANCED_CHANNEL"
author: windows-driver-content
description: The _BRB_L2CA_OPEN_ENHANCED_CHANNEL structure is used to open an enhanced L2CAP channel to a remote device, or send a response for accepting/rejecting an incoming enhanced L2CAP connection request that was initiated by a remote device.
old-location: bltooth\_brb_l2ca_open_enhanced_channel.htm
old-project: bltooth
ms.assetid: 34CA2A3E-871F-46D4-962A-8EE8D7B8DA15
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: BRB_L2CA_OPEN_ENHANCED_CHANNEL, BRB_L2CA_OPEN_ENHANCED_CHANNEL structure [Bluetooth Devices], PBRB_L2CA_OPEN_ENHANCED_CHANNEL, PBRB_L2CA_OPEN_ENHANCED_CHANNEL structure pointer [Bluetooth Devices], _BRB_L2CA_OPEN_ENHANCED_CHANNEL, _BRB_L2CA_OPEN_ENHANCED_CHANNEL structure [Bluetooth Devices], bltooth._brb_l2ca_open_enhanced_channel, bltooth.brb_l2ca_open_enhanced_channel, bthddi/PBRB_L2CA_OPEN_ENHANCED_CHANNEL, bthddi/_BRB_L2CA_OPEN_ENHANCED_CHANNEL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows 8 and later versions of Windows
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Bthddi.h
api_name:
-	BRB_L2CA_OPEN_ENHANCED_CHANNEL
product:
- Windows
targetos: Windows
req.typenames: 
---

# _BRB_L2CA_OPEN_ENHANCED_CHANNEL structure
The _BRB_L2CA_OPEN_ENHANCED_CHANNEL structure is used to open an enhanced L2CAP channel to a remote device, or send a response for accepting/rejecting an incoming enhanced L2CAP connection request that was initiated by a remote device.

## Syntax
```
struct _BRB_L2CA_OPEN_ENHANCED_CHANNEL {
  BRB_HEADER                              Hdr;
  L2CAP_CHANNEL_HANDLE                    ChannelHandle;
  union {
    struct {
      USHORT Response;
      USHORT ResponseStatus;
    };
    USHORT Psm;
  };
  ULONG                                   ChannelFlags;
  BTH_ADDR                                BtAddress;
  struct {
    L2CAP_EXTENDED_FLOW_SPEC ExtendedFlowSpec;
    USHORT                   ExtendedWindowSize;
    PL2CAP_CONFIG_OPTION     ExtraOptions;
    USHORT                   Fcs;
    ULONG                    Flags;
    L2CAP_FLOWSPEC           Flow;
    L2CAP_CONFIG_VALUE_RANGE FlushTO;
    USHORT                   LinkTO;
    L2CAP_CONFIG_VALUE_RANGE Mtu;
    ULONG                    NumExtraOptions;
    struct {
      UCHAR ServiceType;
      ULONG Latency;
    } LocalQos;
    struct {
      ULONG                                 Flags;
      L2CAP_RETRANSMISSION_AND_FLOW_CONTROL RetransmissionAndFlow;
    } ModeConfig;
  } ConfigOut;
  struct {
    ULONG                    Flags;
    L2CAP_CONFIG_RANGE       FlushTO;
    L2CAP_CONFIG_VALUE_RANGE Mtu;
  } ConfigIn;
  ULONG                                   CallbackFlags;
  PFNBTHPORT_INDICATION_CALLBACK_ENHANCED Callback;
  PVOID                                   CallbackContext;
  PVOID                                   ReferenceObject;
  CHANNEL_CONFIG_RESULTS_ENHANCED         OutResults;
  CHANNEL_CONFIG_RESULTS_ENHANCED         InResults;
  UCHAR                                   IncomingQueueDepth;
  PVOID                                   Reserved;
};
```

## Members


`Hdr`

A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536612">BRB_HEADER</a> structure that contains information
     about the current BRB.

`ChannelHandle`

##### 



#######

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

`BtAddress`

The Bluetooth address of the device for which the connection is intended.

`ConfigOut`

The substructure that contains parameter settings for a <b>BRB_L2CA_OPEN_ENHANCED_CHANNEL</b> BRB sent to a remote
     device.



#### Flags

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
<tr>
<td>
CFG_ENHANCED

</td>
<td>
Specifies that the ModeConfig structure is valid.

</td>
</tr>
<tr>
<td>
CFG_FCS

</td>
<td>
Specifies that the Fcs value is valid.

</td>
</tr>
</table>
 



#### Mtu

The range of message transfer units (MTUs) that is used to negotiate the size of the outbound
      half of channel.



#### FlushTO

The range of possible values to be used for the flush timeout for the outbound half of the
      channel.



#### Flow

Reserved for future use. Do not use.



#### LinkTO

The Link Manager link timeout.



#### NumExtraOptions

The number of array items that are contained in the 
      <b>ExtraOptions</b> member. This value should be zero for most clients.



#### ExtraOptions

Extra options. This value should be zero for most clients.



#### Fcs

Specifies whether FCS should be used for the enhanced L2CAP channel. This value is valid only if CM_RETRANSMISSION_AND_FLOW or CM_STREAMING flag is specified in the <b>Flags</b> member.



#### ExtendedFlowSpec

Not supported.



#### ExtendedWindowSize

Not supported.

`ConfigIn`

The substructure that contains parameter settings to validate incoming
     <b>BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE</b> BRBs that are sent from a remote device.



#### Flags

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
 



#### Mtu

The range of message transfer units (MTUs) that is used to negotiate the size of the inbound
      half of channel.



#### FlushTO

The range of possible values to be used for the flush timeout for the inbound half of the
      channel.

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
        options. This flag is used with <b>BRB_L2CA_OPEN_ENHANCED_CHANNEL_RESPONSE</b> BRBs.

</td>
</tr>
<tr>
<td>
CALLBACK_CONFIG_EXTRA_OUT

</td>
<td>
If set, the callback routine will be called when the remote device rejects an extra configuration
        option from a <b>BRB_L2CA_OPEN_ENHANCED_CHANNEL</b> request. If not set and the remote device rejects the
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
If set, the callback routine will be called when a remote device disconnects from the enhanced L2CAP
        channel.

</td>
</tr>
<tr>
<td>
CALLBACK_RECV_PACKET

</td>
<td>
If set, the callback routine will be called when the profile driver receives an incoming enhanced L2CAP
        packet.

</td>
</tr>
</table>

`Callback`

The 
     <a href="https://msdn.microsoft.com/1C08937A-2B0C-4A6C-ACDF-1A751BF0D6F6">Enhanced L2CAP Callback
     Function</a> implemented by the profile driver, that the Bluetooth driver stack should call to notify
     the profile driver about any changes to the enhanced L2CAP connection.

`CallbackContext`

The context to pass to the callback function specified in the 
     <b>Callback</b> member. The profile driver defines this value.

`ReferenceObject`

A pointer to an object to pass to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff558678">ObReferenceObject</a> and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> for which to
     maintain a reference count of.

`OutResults`

A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh450871">CHANNEL_CONFIG_RESULTS_ENHANCED</a> structure that
     contains configuration parameters negotiated for the outbound request.

`InResults`

A CHANNEL_CONFIG_RESULTS_ENHANCED structure that contains configuration parameters negotiated for the inbound
     request.

`IncomingQueueDepth`

Specifies the incoming queue length in message transfer units (MTUs).

`Reserved`

Reserved member. Do not use.

## Remarks
Profile drivers can use CM_BASIC | CM_RETRANSMISSION_AND_FLOW, or CM_BASIC | CM_STREAMING modes for the <b>Flags</b> member. This indicates to open an enhanced retransmission mode, or streaming mode channel if possible, and if not fall back to basic mode channel. 
A value of CM_RETRANSMISSION_AND_FLOW | CM_STREAMING is not supported.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows 8 and later versions of Windows Versions:\_Supported in Windows 8 and later versions of Windows |
| **Header** | bthddi.h (include Bthddi.h) |