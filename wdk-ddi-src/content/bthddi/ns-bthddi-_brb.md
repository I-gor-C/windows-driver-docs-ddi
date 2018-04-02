---
UID: NS:bthddi._BRB
title: "_BRB"
author: windows-driver-content
description: Profile drivers use Bluetooth request blocks (BRBs), to send requests to the Bluetooth driver stack. The BRB structure defines the format for all supported commands that can be sent to a Bluetooth device.
old-location: bltooth\brb.htm
old-project: bltooth
ms.assetid: b9fc6eb9-6793-442a-a736-18929df14f20
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PBRB, BRB, BRB structure [Bluetooth Devices], PBRB, PBRB structure pointer [Bluetooth Devices], _BRB, bltooth.brb, bth_structs_7ccc2ad1-dd10-4ae9-be41-fa79229b32aa.xml, bthddi/BRB, bthddi/PBRB"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows Vista, and later.
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
-	bthddi.h
api_name:
-	BRB
product: Windows
targetos: Windows
req.typenames: BRB, *PBRB
---

# _BRB structure
Profile drivers use Bluetooth request blocks (BRBs), to send requests to the Bluetooth driver stack.
  The BRB structure defines the format for all supported commands that can be sent to a Bluetooth
  device.

## Syntax
```
typedef struct _BRB {
  union {
    _BRB_ACL_ENTER_ACTIVE_MODE       BrbAclEnterActiveMode;
    _BRB_ACL_GET_MODE                BrbAclGetMode;
    _BRB_GET_DEVICE_INTERFACE_STRING BrbGetDeviceInterfaceString;
    _BRB_GET_LOCAL_BD_ADDR           BrbGetLocalBdAddress;
    _BRB_HEADER                      BrbHeader;
    _BRB_L2CA_ACL_TRANSFER           BrbL2caAclTransfer;
    _BRB_L2CA_CLOSE_CHANNEL          BrbL2caCloseChannel;
    _BRB_L2CA_OPEN_CHANNEL           BrbL2caOpenChannel;
    _BRB_L2CA_OPEN_ENHANCED_CHANNEL  BrbL2caOpenEnhancedChannel;
    _BRB_L2CA_PING                   BrbL2caPing;
    _BRB_L2CA_REGISTER_SERVER        BrbL2caRegisterServer;
    _BRB_L2CA_UNREGISTER_SERVER      BrbL2caUnregisterServer;
    _BRB_L2CA_UPDATE_CHANNEL         BrbL2caUpdateChannel;
    _BRB_PSM                         BrbPsm;
    _BRB_SCO_CLOSE_CHANNEL           BrbScoCloseChannel;
    _BRB_SCO_FLUSH_CHANNEL           BrbScoFlushChannel;
    _BRB_SCO_GET_CHANNEL_INFO        BrbScoGetChannelInfo;
    _BRB_SCO_GET_SYSTEM_INFO         BrbScoGetSystemInfo;
    _BRB_SCO_OPEN_CHANNEL            BrbScoOpenChannel;
    _BRB_SCO_REGISTER_SERVER         BrbScoRegisterServer;
    _BRB_SCO_TRANSFER                BrbScoTransfer;
    _BRB_SCO_UNREGISTER_SERVER       BrbScoUnregisterServer;
  };
} BRB, *PBRB;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536612">BRB_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536854">_BRB_ACL_ENTER_ACTIVE_MODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536855">_BRB_ACL_GET_MODE</a>



<a href="https://msdn.microsoft.com/340e4b9a-9959-4eda-b26b-674f7fca7156">
   _BRB_GET_DEVICE_INTERFACE_STRING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536857">_BRB_GET_LOCAL_BD_ADDR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536858">_BRB_L2CA_ACL_TRANSFER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536859">_BRB_L2CA_CLOSE_CHANNEL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536860">_BRB_L2CA_OPEN_CHANNEL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536861">_BRB_L2CA_PING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536862">_BRB_L2CA_REGISTER_SERVER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536863">_BRB_L2CA_UNREGISTER_SERVER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536864">_BRB_L2CA_UPDATE_CHANNEL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536865">_BRB_PSM</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536866">_BRB_SCO_CLOSE_CHANNEL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536867">_BRB_SCO_FLUSH_CHANNEL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536868">_BRB_SCO_GET_CHANNEL_INFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536869">_BRB_SCO_GET_SYSTEM_INFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536870">_BRB_SCO_OPEN_CHANNEL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536871">_BRB_SCO_REGISTER_SERVER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536872">_BRB_SCO_TRANSFER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536873">_BRB_SCO_UNREGISTER_SERVER</a>