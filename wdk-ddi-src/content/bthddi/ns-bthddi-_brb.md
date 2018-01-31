---
UID : NS:bthddi._BRB
title : "_BRB"
author : windows-driver-content
description : Profile drivers use Bluetooth request blocks (BRBs), to send requests to the Bluetooth driver stack. The BRB structure defines the format for all supported commands that can be sent to a Bluetooth device.
old-location : bltooth\brb.htm
old-project : bltooth
ms.assetid : b9fc6eb9-6793-442a-a736-18929df14f20
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : bltooth.brb, bthddi/BRB, bth_structs_7ccc2ad1-dd10-4ae9-be41-fa79229b32aa.xml, bthddi/PBRB, PBRB structure pointer [Bluetooth Devices], BRB structure [Bluetooth Devices], _BRB, BRB, PBRB, *PBRB
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bthddi.h
req.include-header : Bthddi.h
req.target-type : Windows
req.target-min-winverclnt : Versions:\_Supported in Windows Vista, and later.
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
req.typenames : BRB, *PBRB
---

# _BRB structure
Profile drivers use Bluetooth request blocks (BRBs), to send requests to the Bluetooth driver stack.
  The BRB structure defines the format for all supported commands that can be sent to a Bluetooth
  device.

## Syntax
````
typedef struct _BRB {
  union {
    struct _BRB_HEADER  BrbHeader;
    struct _BRB_GET_DEVICE_INTERFACE_STRING  BrbGetDeviceInterfaceString;
    struct _BRB_L2CA_REGISTER_SERVER  BrbL2caRegisterServer;
    struct _BRB_L2CA_UNREGISTER_SERVER  BrbL2caUnregisterServer;
    struct _BRB_L2CA_OPEN_CHANNEL  BrbL2caOpenChannel;
    struct _BRB_L2CA_CLOSE_CHANNEL  BrbL2caCloseChannel;
    struct _BRB_L2CA_PING  BrbL2caPing;
    struct _BRB_L2CA_ACL_TRANSFER  BrbL2caAclTransfer;
    struct _BRB_GET_LOCAL_BD_ADDR  BrbGetLocalBdAddress;
    struct _BRB_PSM  BrbPsm;
    struct _BRB_L2CA_UPDATE_CHANNEL  BrbL2caUpdateChannel;
    struct _BRB_SCO_REGISTER_SERVER  BrbScoRegisterServer;
    struct _BRB_SCO_UNREGISTER_SERVER  BrbScoUnregisterServer;
    struct _BRB_SCO_OPEN_CHANNEL  BrbScoOpenChannel;
    struct _BRB_SCO_CLOSE_CHANNEL  BrbScoCloseChannel;
    struct _BRB_SCO_FLUSH_CHANNEL  BrbScoFlushChannel;
    struct _BRB_SCO_TRANSFER  BrbScoTransfer;
    struct _BRB_SCO_GET_CHANNEL_INFO  BrbScoGetChannelInfo;
    struct _BRB_SCO_GET_SYSTEM_INFO  BrbScoGetSystemInfo;
    struct _BRB_ACL_GET_MODE  BrbAclGetMode;
    struct _BRB_ACL_ENTER_ACTIVE_MODE  BrbAclEnterActiveMode;
    struct _BRB_L2CA_OPEN_ENHANCED_CHANNEL  BrbL2caOpenEnhancedChannel;
  };
} BRB, *PBRB;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="..\bthddi\ns-bthddi-_brb_l2ca_close_channel.md">_BRB_L2CA_CLOSE_CHANNEL</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_get_channel_info.md">_BRB_SCO_GET_CHANNEL_INFO</a>

<a href="..\bthddi\ns-bthddi-_brb_l2ca_open_channel.md">_BRB_L2CA_OPEN_CHANNEL</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_get_system_info.md">_BRB_SCO_GET_SYSTEM_INFO</a>

<a href="..\bthddi\ns-bthddi-_brb_l2ca_acl_transfer.md">_BRB_L2CA_ACL_TRANSFER</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_flush_channel.md">_BRB_SCO_FLUSH_CHANNEL</a>

<a href="..\bthddi\ns-bthddi-_brb_header.md">BRB_HEADER</a>

<a href="..\bthddi\ns-bthddi-_brb_psm.md">_BRB_PSM</a>

<a href="..\bthddi\ns-bthddi-_brb_acl_enter_active_mode.md">_BRB_ACL_ENTER_ACTIVE_MODE</a>

<mshelp:link keywords="bltooth._brb_get_device_interface_string" tabindex="0"><b>
   _BRB_GET_DEVICE_INTERFACE_STRING</b></mshelp:link>

<a href="..\bthddi\ns-bthddi-_brb_l2ca_unregister_server.md">_BRB_L2CA_UNREGISTER_SERVER</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_close_channel.md">_BRB_SCO_CLOSE_CHANNEL</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_unregister_server.md">_BRB_SCO_UNREGISTER_SERVER</a>

<a href="..\bthddi\ns-bthddi-_brb_l2ca_ping.md">_BRB_L2CA_PING</a>

<a href="..\bthddi\ns-bthddi-_brb_get_local_bd_addr.md">_BRB_GET_LOCAL_BD_ADDR</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_open_channel.md">_BRB_SCO_OPEN_CHANNEL</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_transfer.md">_BRB_SCO_TRANSFER</a>

<a href="..\bthddi\ns-bthddi-_brb_sco_register_server.md">_BRB_SCO_REGISTER_SERVER</a>

<a href="..\bthddi\ns-bthddi-_brb_l2ca_register_server.md">_BRB_L2CA_REGISTER_SERVER</a>

<a href="..\bthddi\ns-bthddi-_brb_acl_get_mode.md">_BRB_ACL_GET_MODE</a>

<a href="..\bthddi\ns-bthddi-_brb_l2ca_update_channel.md">_BRB_L2CA_UPDATE_CHANNEL</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BRB structure%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>