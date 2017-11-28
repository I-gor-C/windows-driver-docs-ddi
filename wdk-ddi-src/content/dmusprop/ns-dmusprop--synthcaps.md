---
UID: NS.dmusprop._SYNTHCAPS
title: SYNTHCAPS
author: windows-driver-content
description: The SYNTHCAPS structure specifies the capabilities of a synthesizer.
old-location: audio\synthcaps.htm
old-project: audio
ms.assetid: d9d7327f-a413-4828-b204-e08198d0fe9e
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: SYNTHCAPS, SYNTHCAPS, *PSYNTHCAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dmusprop.h
req.include-header: Dmusprop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SYNTHCAPS
req.alt-loc: dmusprop.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: ISynthSinkDMus
---

# SYNTHCAPS structure



## -description
<p>The SYNTHCAPS structure specifies the capabilities of a synthesizer.</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>Guid</b>

<dd>
<p>Specifies the class ID for the synthesizer's miniport driver interface.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the general capabilities of the driver. This member is a bitfield whose value is either zero or the bitwise OR of one or more of the following flag bits:</p>
<p></p>
<dl>

### -field <a id="SYNTH_PC_DLS"></a><a id="synth_pc_dls"></a>SYNTH_PC_DLS

<dd>
<p>The driver supports downloadable sample collections (DLS Level 1).</p>
</dd>

### -field <a id="SYNTH_PC_EXTERNAL"></a><a id="synth_pc_external"></a>SYNTH_PC_EXTERNAL

<dd>
<p>The synth represents a connection to external hardware.</p>
</dd>

### -field <a id="SYNTH_PC_SOFTWARESYNTH"></a><a id="synth_pc_softwaresynth"></a>SYNTH_PC_SOFTWARESYNTH

<dd>
<p>The driver implements a software synthesizer.</p>
</dd>

### -field <a id="SYNTH_PC_MEMORYSIZEFIXED"></a><a id="synth_pc_memorysizefixed"></a>SYNTH_PC_MEMORYSIZEFIXED

<dd>
<p>The memory size given in the <b>MemorySize</b> member is valid and represents the maximum amount of sample memory in bytes. This flag is typically set when the sample memory is not system memory.</p>
</dd>

### -field <a id="SYNTH_PC_GMINHARDWARE"></a><a id="synth_pc_gminhardware"></a>SYNTH_PC_GMINHARDWARE

<dd>
<p>The synth supports the General MIDI sound set in hardware.</p>
</dd>

### -field <a id="SYNTH_PC_GSINHARDWARE"></a><a id="synth_pc_gsinhardware"></a>SYNTH_PC_GSINHARDWARE

<dd>
<p>The synth supports the Roland GS sound set in hardware.</p>
</dd>

### -field <a id="SYNTH_PC_REVERB"></a><a id="synth_pc_reverb"></a>SYNTH_PC_REVERB

<dd>
<p>The synth supports reverb.</p>
</dd>

### -field <a id="SYNTH_PC_DLS2"></a><a id="synth_pc_dls2"></a>SYNTH_PC_DLS2

<dd>
<p>The driver supports downloadable sample collections (DLS Level 2).</p>
</dd>

### -field <a id="SYNTH_PC_SYSTEMMEMORY"></a><a id="synth_pc_systemmemory"></a>SYNTH_PC_SYSTEMMEMORY

<dd>
<p>The synth can use system memory.</p>
</dd>
</dl>
</dd>

### -field <b>MemorySize</b>

<dd>
<p>Specifies the amount of sample memory on the device (in bytes). This field should contain the value SYNTH_PC_SYSTEMMEMORY if the device uses system memory for sample memory with no limitation on the amount of memory allocated.</p>
</dd>

### -field <b>MaxChannelGroups</b>

<dd>
<p>Specifies the maximum number of channel groups this driver supports. Each channel group represents a set of 16 MIDI channels and has associated with it all the state that a MIDI hardware device would keep, which includes DLS, GM, GS, XG, or other mode information. DLS downloads, however, are per-driver and can be used by any of the channel groups. This prevents wasting memory by downloading several copies of the same DLS sample, one per channel group.</p>
</dd>

### -field <b>MaxVoices</b>

<dd>
<p>Specifies the maximum number of voices that the rendering device supports. If the property handler is unable to provide a valid number for this member, it should set the member to (ULONG)-1.</p>
</dd>

### -field <b>MaxAudioChannels</b>

<dd>
<p>Specifies the maximum number of audio channels that the rendering device supports. If the property handler is unable to provide a valid number for this member, it should set the member to (ULONG)-1.</p>
</dd>

### -field <b>EffectFlags</b>

<dd>
<p>Specifies the effects that the rendering device is capable of producing. This member is a bitfield whose value is either zero or the bitwise OR of the following flag bits:</p>
<p></p>
<dl>

### -field <a id="SYNTH_EFFECT_REVERB"></a><a id="synth_effect_reverb"></a>SYNTH_EFFECT_REVERB

<dd>
<p>Rendering device can produce reverb effect.</p>
</dd>

### -field <a id="SYNTH_EFFECT_CHORUS"></a><a id="synth_effect_chorus"></a>SYNTH_EFFECT_CHORUS

<dd>
<p>Rendering device can produce chorus effect.</p>
</dd>

### -field <a id="SYNTH_EFFECT_DELAY"></a><a id="synth_effect_delay"></a>SYNTH_EFFECT_DELAY

<dd>
<p>Rendering device can produce delay effect.</p>
</dd>
</dl>
<p>If the device supports none of these capabilities, set this member to SYNTH_EFFECT_NONE (zero).</p>
</dd>

### -field <b>Description</b>

<dd>
<p>Contains a text description of the device. This member is a WCHAR array containing a null-terminated string (for example, "Microsoft MPU-401").</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537389">KSPROPERTY_SYNTH_CAPS</a> get-property request uses the SYNTHCAPS structure to retrieve the capabilities of a synthesizer device from a DMus miniport driver.</p>

<p>SYNTH_CAPS is similar to the DMUS_PORTCAPS structure, which is described in the Microsoft Windows SDK documentation.</p>

<p>In the DMusUART sample driver in the Windows Driver Kit (WDK), the KSPROPERTY_SYNTH_CAPS property handler sets the members of the SYNTHCAPS structure to the following values:</p>

<p>In this example, the 0xFFFFFFFF values indicate that the handler has no way of knowing the actual <b>MaxVoices</b> and <b>MaxAudioChannels</b> limits because they are completely dependent on whatever external synthesizer happens to be connected to the UART. Elsewhere in the code, but not shown in the preceding example, the DMusUART property handler sets the <b>Guid</b> member of the SYNTHCAPS structure to either <b>CLSID_MiniportDriverDMusUART</b> or <b>CLSID_MiniportDriverDMusUARTCapture</b>. The one the <b>Guid</b> member is it is set to depends on whether the target node (of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537203">KSNODETYPE_SYNTHESIZER</a>) for the property request lies on a data path that handles rendering data or capture data. Both class IDs are defined in header file Dmusicks.h.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537389">KSPROPERTY_SYNTH_CAPS</a> get-property request uses the SYNTHCAPS structure to retrieve the capabilities of a synthesizer device from a DMus miniport driver.</p>

<p>SYNTH_CAPS is similar to the DMUS_PORTCAPS structure, which is described in the Microsoft Windows SDK documentation.</p>

<p>In the DMusUART sample driver in the Windows Driver Kit (WDK), the KSPROPERTY_SYNTH_CAPS property handler sets the members of the SYNTHCAPS structure to the following values:</p>

<p>In this example, the 0xFFFFFFFF values indicate that the handler has no way of knowing the actual <b>MaxVoices</b> and <b>MaxAudioChannels</b> limits because they are completely dependent on whatever external synthesizer happens to be connected to the UART. Elsewhere in the code, but not shown in the preceding example, the DMusUART property handler sets the <b>Guid</b> member of the SYNTHCAPS structure to either <b>CLSID_MiniportDriverDMusUART</b> or <b>CLSID_MiniportDriverDMusUARTCapture</b>. The one the <b>Guid</b> member is it is set to depends on whether the target node (of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537203">KSNODETYPE_SYNTHESIZER</a>) for the property request lies on a data path that handles rendering data or capture data. Both class IDs are defined in header file Dmusicks.h.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusprop.h (include Dmusprop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537389">KSPROPERTY_SYNTH_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537203">KSNODETYPE_SYNTHESIZER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20SYNTHCAPS structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
