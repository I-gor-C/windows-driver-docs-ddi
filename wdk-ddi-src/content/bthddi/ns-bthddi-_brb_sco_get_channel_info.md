---
UID : NS:bthddi._BRB_SCO_GET_CHANNEL_INFO
title : _BRB_SCO_GET_CHANNEL_INFO
author : windows-driver-content
description : The _BRB_SCO_GET_CHANNEL_INFO structure describes the settings and statistics of a SCO channel.
old-location : bltooth\_brb_sco_get_channel_info.htm
old-project : bltooth
ms.assetid : 1a7eb79c-5a3e-4977-ba1f-682bbebb0494
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : _BRB_SCO_GET_CHANNEL_INFO,
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
req.alt-api : _BRB_SCO_GET_CHANNEL_INFO
req.alt-loc : bthddi.h
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
req.typenames : 
---

# _BRB_SCO_GET_CHANNEL_INFO structure
The _BRB_SCO_GET_CHANNEL_INFO structure describes the settings and statistics of a SCO
  channel.

## Syntax
````
struct _BRB_SCO_GET_CHANNEL_INFO {
  BRB_HEADER                Hdr;
  BTH_ADDR                  BtAddress;
  SCO_CHANNEL_HANDLE        ChannelHandle;
  ULONG                     InfoFlags;
  ULONG                     TransmitBandwidth;
  ULONG                     ReceiveBandwidth;
  USHORT                    MaxLatency;
  USHORT                    PacketType;
  USHORT                    ContentFormat;
  USHORT                    Reserved;
  SCO_RETRANSMISSION_EFFORT RetransmissionEffort;
  ULONG                     ChannelFlags;
  CONNECTION_HANDLE         HciConnectionHandle;
  SCO_LINK_TYPE             LinkType;
  BASEBAND_CHANNEL_INFO     BasebandInfo;
};
````

## Members

        
            `BasebandInfo`

            A 
     <a href="..\bthddi\ns-bthddi-_baseband_channel_info.md">BASEBAND_CHANNEL_INFO</a> structure that
     contains information for the SCO connection. This information is only available for links established
     using the 1.2 Bluetooth Synchronous Commands.
        
            `BtAddress`

            The Bluetooth address of the remote device.
        
            `ChannelFlags`

            Flags that specify how the channel was opened. Valid flag values are listed in the following
     table.
     

<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
SCO_CF_LINK_AUTHENTICATED

</td>
<td>
The link must be authenticated.

</td>
</tr>
<tr>
<td>
SCO_CF_LINK_ENCRYPTED

</td>
<td>
The link must be encrypted. Setting this flag also sets the SCO_CF_LINK_AUTHENTICATED flag.

</td>
</tr>
<tr>
<td>
SCO_CF_LINK_SUPPRESS_PIN

</td>
<td>
The profile driver indicates its preference that users not be prompted for a PIN.

</td>
</tr>
</table>
        
            `ChannelHandle`

            The handle to the SCO channel to query.
        
            `ContentFormat`

            The audio voice setting for the channel. Use the following definitions to decode this member:
        
            `HciConnectionHandle`

            The host controller interface's connection handle for the SCO connection.
        
            `Hdr`

            A 
     <a href="..\bthddi\ns-bthddi-_brb_header.md">BRB_HEADER</a> structure that contains information
     about the current BRB.
        
            `InfoFlags`

            A flag that determines if baseband information is available for the SCO channel. The following
     flag is defined:
     

<table>
<tr>
<th>
       Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
SCO_INFO_BASEBAND_AVAILABLE

</td>
<td>
If set, baseband settings are available for the SCO channel.

</td>
</tr>
</table>
        
            `LinkType`

            The 
     <a href="..\bthddi\ne-bthddi-_sco_link_type.md">SCO_LINK_TYPE</a> that is associated with the host
     controller interface.
        
            `MaxLatency`

            A value that represents the upper limit of the sum of the synchronous interval and the size of the
     SCO window, in milliseconds. Possible values are listed in the following table.
     

<table>
<tr>
<th>
       Values</th>
<th>Description</th>
</tr>
<tr>
<td>
0x0000 to 0x0003

</td>
<td>
Reserved for future use.

</td>
</tr>
<tr>
<td>
0x0004 to 0xFFFE

</td>
<td>
The range of latency values for the channel.

</td>
</tr>
<tr>
<td>
0xFFFF

</td>
<td>
The channel doesn't have a preferred 
        <b>MaxLatency</b> setting.

</td>
</tr>
</table>
        
            `PacketType`

            A flag or combination of flags that indicates the type of data packets that the SCO channel
     supports. These SCO packet types are defined by the Bluetooth SIG. See the Bluetooth specification for
     more information about these flags. Possible values include:
        
            `ReceiveBandwidth`

            The reception bandwidth of the channel, in bytes per second.
        
            `Reserved`

            Reserved for future use. Do not use.
        
            `RetransmissionEffort`

            A 
     <a href="..\bthddi\ne-bthddi-_sco_retransmission_effort.md">SCO_RETRANSMISSION_EFFORT</a> value that
     determines the channel's retransmission policies.
        
            `TransmitBandwidth`

            The transmission bandwidth of the channel, in bytes per second.

    ## Remarks
        To get the settings and statistics of a SCO channel, profile drivers should 
    <a href="https://msdn.microsoft.com/53a692e7-9c71-4dca-9331-32ac97b94179">build and send</a> a 
    <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff536868">
    BRB_SCO_GET_CHANNEL_INFO</a> request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bthddi.h (include Bthddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\bthddi\ns-bthddi-_brb_header.md">BRB_HEADER</a>
</dt>
<dt>
<a href="..\bthddi\ne-bthddi-_sco_retransmission_effort.md">SCO_RETRANSMISSION_EFFORT</a>
</dt>
<dt>
<a href="..\bthddi\ne-bthddi-_sco_link_type.md">SCO_LINK_TYPE</a>
</dt>
<dt>
<a href="..\bthddi\ns-bthddi-_baseband_channel_info.md">BASEBAND_CHANNEL_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff536868">BRB_SCO_GET_CHANNEL_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20_BRB_SCO_GET_CHANNEL_INFO structure%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>