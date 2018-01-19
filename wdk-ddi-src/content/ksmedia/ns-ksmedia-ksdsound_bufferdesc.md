---
UID : NS:ksmedia.KSDSOUND_BUFFERDESC
title : KSDSOUND_BUFFERDESC
author : windows-driver-content
description : The KSDSOUND_BUFFERDESC structure describes a DirectSound buffer.
old-location : audio\ksdsound_bufferdesc.htm
old-project : audio
ms.assetid : 95b2f2ff-b98f-4210-9a4f-898573679aa7
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : KSDSOUND_BUFFERDESC, KSDSOUND_BUFFERDESC, *PKSDSOUND_BUFFERDESC
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksmedia.h
req.include-header : Ksmedia.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSDSOUND_BUFFERDESC
req.alt-loc : ksmedia.h
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
req.typenames : KSDSOUND_BUFFERDESC, *PKSDSOUND_BUFFERDESC
---

# KSDSOUND_BUFFERDESC structure
The KSDSOUND_BUFFERDESC structure describes a DirectSound buffer.

## Syntax
````
typedef struct {
  ULONG        Flags;
  ULONG        Control;
  WAVEFORMATEX WaveFormatEx;
} KSDSOUND_BUFFERDESC, *PKSDSOUND_BUFFERDESC;
````

## Members

        
            `Control`

            Specifies the capabilities of the buffer. The capabilities of a buffer are represented by a set of control flags. This member can be set to the bitwise OR of one or more of the following flag bits:
        
            `Flags`

            Specifies the buffer configuration. This member can be set to the bitwise OR of one or more of the following flag bits:
        
            `WaveFormatEx`

            Specifies the wave-data format of the buffer. This member is a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff538799">WAVEFORMATEX</a>.

    ## Remarks
        The <a href="..\ksmedia\ns-ksmedia-ksdataformat_dsound.md">KSDATAFORMAT_DSOUND</a> structure contains a <b>BufferDesc</b> member that is a KSDSOUND_BUFFERDESC structure.

Note that the <b>WaveFormatEx</b> member of the KSDSOUND_BUFFERDESC structure can be extended to include additional format information (for example, a channel configuration mask). For details, see <a href="..\ksmedia\ns-ksmedia-waveformatextensible.md">WAVEFORMATEXTENSIBLE</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h (include Ksmedia.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ksmedia\ns-ksmedia-ksdataformat_dsound.md">KSDATAFORMAT_DSOUND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537148">KSNODETYPE_3D_EFFECTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537482">KSPROPSETID_Hrtf3d</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537190">KSNODETYPE_SRC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537297">KSPROPERTY_AUDIO_POSITION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538799">WAVEFORMATEX</a>
</dt>
<dt>
<a href="..\ksmedia\ns-ksmedia-waveformatextensible.md">WAVEFORMATEXTENSIBLE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSDSOUND_BUFFERDESC structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>