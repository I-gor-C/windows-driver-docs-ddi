# Declarations in the dmusicks header
This header Dmusicks contains these programming interfaces:

Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IPortDMus interface](nn-dmusicks-iportdmus.md) | TBD |
| [IMasterClock interface](nn-dmusicks-imasterclock.md) | TBD |
| [IMiniportDMus interface](nn-dmusicks-iminiportdmus.md) | TBD |
| [IPositionNotify interface](nn-dmusicks-ipositionnotify.md) | TBD |
| [IMXF interface](nn-dmusicks-imxf~r1.md) | TBD |
| [IAllocatorMXF interface](nn-dmusicks-iallocatormxf~r1.md) | TBD |
| [ISynthSinkDMus interface](nn-dmusicks-isynthsinkdmus.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [DMUS_STREAM_TYPE enumeration](ne-dmusicks-dmus-stream-type.md) | Used for a DirectMusic synthesizer device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IAllocatorMXF::GetMessage method](nf-dmusicks-iallocatormxf-getmessage.md) | The GetMessage method serves as the retrieval point for any DirectMusic kernel-mode component that utilizes the port driver's allocator to reuse DMUS_KERNEL_EVENT structures. |
| [ISynthSinkDMus::SyncToMaster method](nf-dmusicks-isynthsinkdmus-synctomaster.md) | The SyncToMaster method allows synchronization to the master clock in order to avoid drift. |
| [IPortDMus::Notify method](nf-dmusicks-iportdmus-notify.md) | The Notify method should be called from the miniport driver's interrupt service routine (ISR) when a hardware interrupt has occurred. |
| [IMiniportDMus::Service method](nf-dmusicks-iminiportdmus-service.md) | This method does not currently need to be implemented in the miniport driver. The Service method is currently unused. |
| [IAllocatorMXF::GetBuffer method](nf-dmusicks-iallocatormxf-getbuffer.md) | The GetBuffer method allocates a buffer for long MIDI events. |
| [CLEAR_PACKAGE_EVT function](nf-dmusicks-clear-package-evt.md) | TBD |
| [IMasterClock::GetTime method](nf-dmusicks-imasterclock-gettime.md) | The GetTime method retrieves the current reference time read from the master clock. |
| [ISynthSinkDMus::RefTimeToSample method](nf-dmusicks-isynthsinkdmus-reftimetosample.md) | The RefTimeToSample method converts a reference time into a sample time. |
| [ISynthSinkDMus::SampleToRefTime method](nf-dmusicks-isynthsinkdmus-sampletoreftime.md) | The SampleToRefTime method converts a sample time to a reference time. |
| [IPortDMus::RegisterServiceGroup method](nf-dmusicks-iportdmus-registerservicegroup.md) | The RegisterServiceGroup method registers a service group with the DMus port driver. |
| [IAllocatorMXF::PutBuffer method](nf-dmusicks-iallocatormxf-putbuffer.md) | This method is not currently used by the miniport driver. The PutBuffer method passes a buffer to the allocator, but this occurs automatically when IMXF |
| [PACKAGE_EVT function](nf-dmusicks-package-evt.md) | TBD |
| [IMiniportDMus::Init method](nf-dmusicks-iminiportdmus-init.md) | The Init method initializes the DMus miniport object. |
| [SET_INCOMPLETE_EVT function](nf-dmusicks-set-incomplete-evt.md) | TBD |
| [IMiniportDMus::NewStream method](nf-dmusicks-iminiportdmus-newstream.md) | The NewStream method creates a new instance of a logical stream associated with a specified physical channel. |
| [ISynthSinkDMus::Render method](nf-dmusicks-isynthsinkdmus-render.md) | The Render method renders wave data into a destination sink. |
| [IPositionNotify::PositionNotify method](nf-dmusicks-ipositionnotify-positionnotify.md) | Byte position notify for MXF graph. |
| [COMPLETE_EVT function](nf-dmusicks-complete-evt.md) | TBD |
| [SET_PACKAGE_EVT function](nf-dmusicks-set-package-evt.md) | TBD |
| [INCOMPLETE_EVT function](nf-dmusicks-incomplete-evt.md) | TBD |
| [SET_COMPLETE_EVT function](nf-dmusicks-set-complete-evt.md) | TBD |
| [SHORT_EVT function](nf-dmusicks-short-evt.md) | TBD |
| [IAllocatorMXF::GetBufferSize method](nf-dmusicks-iallocatormxf-getbuffersize.md) | The GetBufferSize method gets the buffer size from the allocator. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [IAllocatorMXF structure](ns-dmusicks-iallocatormxf.md) | TBD |
| [IMXF structure](ns-dmusicks-imxf.md) | TBD |
| [DMUS_KERNEL_EVENT structure](ns-dmusicks--dmus-kernel-event.md) | The DMUS_KERNEL_EVENT structure is used to package time-stamped music events. |

This header is used in these topics:

- [audio](..content/_audio)
