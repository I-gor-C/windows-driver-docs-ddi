---
UID : NS:dmusprop._SYNTHCAPS
title : _SYNTHCAPS
author : windows-driver-content
description : The SYNTHCAPS structure specifies the capabilities of a synthesizer.
old-location : audio\synthcaps.htm
old-project : audio
ms.assetid : d9d7327f-a413-4828-b204-e08198d0fe9e
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _SYNTHCAPS, *PSYNTHCAPS, SYNTHCAPS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : dmusprop.h
req.include-header : Dmusprop.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SYNTHCAPS
req.alt-loc : dmusprop.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSYNTHCAPS, SYNTHCAPS"
---

# _SYNTHCAPS structure
The SYNTHCAPS structure specifies the capabilities of a synthesizer.

## Syntax
````
typedef struct _SYNTHCAPS {
  GUID  Guid;
  DWORD Flags;
  DWORD MemorySize;
  DWORD MaxChannelGroups;
  DWORD MaxVoices;
  DWORD MaxAudioChannels;
  DWORD EffectFlags;
  WCHAR Description[128];
} SYNTHCAPS, *PSYNTHCAPS;
````

## Members

        
            `Description`

            Contains a text description of the device. This member is a WCHAR array containing a null-terminated string (for example, "Microsoft MPU-401").
        
            `EffectFlags`

            Specifies the effects that the rendering device is capable of producing. This member is a bitfield whose value is either zero or the bitwise OR of the following flag bits:
        
            `Flags`

            Specifies the general capabilities of the driver. This member is a bitfield whose value is either zero or the bitwise OR of one or more of the following flag bits:
        
            `Guid`

            Specifies the class ID for the synthesizer's miniport driver interface.
        
            `MaxAudioChannels`

            Specifies the maximum number of audio channels that the rendering device supports. If the property handler is unable to provide a valid number for this member, it should set the member to (ULONG)-1.
        
            `MaxChannelGroups`

            Specifies the maximum number of channel groups this driver supports. Each channel group represents a set of 16 MIDI channels and has associated with it all the state that a MIDI hardware device would keep, which includes DLS, GM, GS, XG, or other mode information. DLS downloads, however, are per-driver and can be used by any of the channel groups. This prevents wasting memory by downloading several copies of the same DLS sample, one per channel group.
        
            `MaxVoices`

            Specifies the maximum number of voices that the rendering device supports. If the property handler is unable to provide a valid number for this member, it should set the member to (ULONG)-1.
        
            `MemorySize`

            Specifies the amount of sample memory on the device (in bytes). This field should contain the value SYNTH_PC_SYSTEMMEMORY if the device uses system memory for sample memory with no limitation on the amount of memory allocated.

    ## Remarks
        The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537389">KSPROPERTY_SYNTH_CAPS</a> get-property request uses the SYNTHCAPS structure to retrieve the capabilities of a synthesizer device from a DMus miniport driver.

SYNTH_CAPS is similar to the DMUS_PORTCAPS structure, which is described in the Microsoft Windows SDK documentation.

In the DMusUART sample driver in the Windows Driver Kit (WDK), the KSPROPERTY_SYNTH_CAPS property handler sets the members of the SYNTHCAPS structure to the following values:

In this example, the 0xFFFFFFFF values indicate that the handler has no way of knowing the actual <b>MaxVoices</b> and <b>MaxAudioChannels</b> limits because they are completely dependent on whatever external synthesizer happens to be connected to the UART. Elsewhere in the code, but not shown in the preceding example, the DMusUART property handler sets the <b>Guid</b> member of the SYNTHCAPS structure to either <b>CLSID_MiniportDriverDMusUART</b> or <b>CLSID_MiniportDriverDMusUARTCapture</b>. The one the <b>Guid</b> member is it is set to depends on whether the target node (of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537203">KSNODETYPE_SYNTHESIZER</a>) for the property request lies on a data path that handles rendering data or capture data. Both class IDs are defined in header file Dmusicks.h.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dmusprop.h (include Dmusprop.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537389">KSPROPERTY_SYNTH_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537203">KSNODETYPE_SYNTHESIZER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20SYNTHCAPS structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>