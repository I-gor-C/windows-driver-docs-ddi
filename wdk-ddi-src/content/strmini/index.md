---
UID : NA:strmini
ms.assetid : 5ad00d3a-f0d1-3a8a-b3a7-7b92cf31e96c
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# strmini.h header



strmini.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [PHW_CANCEL_SRB](nc-strmini-phw_cancel_srb.md) | The class driver calls the minidriver's StrMiniCancelPacket routine to signal that a stream request has been canceled. |
| [PHW_EVENT_ROUTINE](nc-strmini-phw_event_routine.md) | The class driver calls the stream minidriver's StrMiniEvent routine to signal to a minidriver an event should be enabled or disabled. |
| [PHW_INTERRUPT](nc-strmini-phw_interrupt.md) | StrMiniInterrupt is the minidriver's interrupt service routine. |
| [PHW_PRIORITY_ROUTINE](nc-strmini-phw_priority_routine.md) | StrMiniPriorityRoutine is a minidriver-supplied callback routine to be executed at a specified priority level. |
| [PHW_QUERY_CLOCK_ROUTINE](nc-strmini-phw_query_clock_routine.md) | Each stream may have a clock associated to it. The class driver queries the clock by calling the stream minidriver-supplied StrMiniClock function, provided in each stream's HW_STREAM_OBJECT. |
| [PHW_RECEIVE_DEVICE_SRB](nc-strmini-phw_receive_device_srb.md) | The stream class driver calls the minidriver's StrMiniReceiveStreamControlPacket routine to handle I/O requests for a specific stream. |
| [PHW_REQUEST_TIMEOUT_HANDLER](nc-strmini-phw_request_timeout_handler.md) | The stream class driver calls the minidriver's StrMiniRequestTimeout routine to signal to the minidriver that a request has timed out. |
| [StreamClassAbortOutstandingRequests](nf-strmini-streamclassabortoutstandingrequests.md) | The StreamClassAbortOutstandingRequests routine aborts all outstanding requests, either to a particular stream, or to the entire driver. |
| [StreamClassCallAtNewPriority](nf-strmini-streamclasscallatnewpriority.md) | The StreamClassCallAtNewPriority routine schedules a routine to be called at a different priority. |
| [StreamClassCompleteRequestAndMarkQueueReady](nf-strmini-streamclasscompleterequestandmarkqueueready.md) | The StreamClassCompleteRequestAndMarkQueueReady routine completes a request, and signals the class driver that the minidriver is ready to receive a new request of the same type. |
| [StreamClassDebugAssert](nf-strmini-streamclassdebugassert.md) | A minidriver can use the StreamClassDebugAssert routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger. |
| [StreamClassDebugPrint](nf-strmini-streamclassdebugprint.md) | In a checked build environment, the minidriver can use the StreamClassDebugPrint routine to print debug messages to the application window and to the Debugger Command window. |
| [StreamClassDeviceNotification](nf-strmini-streamclassdevicenotification.md) | Minidrivers use the StreamClassDeviceNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |
| [StreamClassFilterReenumerateStreams](nf-strmini-streamclassfilterreenumeratestreams.md) | Obsolete. Do not use. |
| [StreamClassGetDmaBuffer](nf-strmini-streamclassgetdmabuffer.md) | The StreamClassGetDmaBuffer routine returns a pointer to the DMA buffer that the class driver allocates for the minidriver. |
| [StreamClassGetNextEvent](nf-strmini-streamclassgetnextevent.md) | Minidrivers can use the StreamClassGetNextEvent routine to search the event queue of a device or of a particular stream. |
| [StreamClassGetPhysicalAddress](nf-strmini-streamclassgetphysicaladdress.md) | The StreamClassGetPhysicalAddress routine translates a virtual memory address to a physical memory address and locks the corresponding physical memory for a DMA operation. |
| [StreamClassQueryMasterClock](nf-strmini-streamclassquerymasterclock.md) | When the minidriver calls the StreamClassQueryMasterClock routine, the class driver queries the appropriate time value of the master clock asynchronously, and passes the result to the routine passed in the ClockCallbackRoutine parameter. |
| [StreamClassQueryMasterClockSync](nf-strmini-streamclassquerymasterclocksync.md) | The minidriver may call the StreamClassQueryMasterClockSync routine to synchronously query a stream's master clock. |
| [StreamClassReadWriteConfig](nf-strmini-streamclassreadwriteconfig.md) | The StreamClassReadWriteConfig routine reads or writes configuration data for the minidriver's parent bus driver. |
| [StreamClassReenumerateStreams](nf-strmini-streamclassreenumeratestreams.md) | Obsolete. Do not use. |
| [StreamClassRegisterAdapter](nf-strmini-streamclassregisteradapter.md) | The StreamClassRegisterAdapter routine registers a stream class minidriver. |
| [StreamClassRegisterFilterWithNoKSPins](nf-strmini-streamclassregisterfilterwithnokspins.md) | The StreamClassRegisterFilterWithNoKSPins routine is used to register filter drivers with Microsoft DirectShow that have no kernel streaming pins and, therefore, do not stream in kernel mode. |
| [StreamClassScheduleTimer](nf-strmini-streamclassscheduletimer.md) | The minidriver calls the StreamClassScheduleTimer routine to schedule a timer, and to specify a routine that is called when the timer expires. |
| [StreamClassStreamNotification](nf-strmini-streamclassstreamnotification.md) | Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |



## Structures
| Title | Description |
| ---- |:---- |
| [_HW_CLOCK_OBJECT](ns-strmini-_hw_clock_object.md) | The HW_CLOCK_OBJECT structure describes the clock associated with a stream. |
| [_HW_EVENT_DESCRIPTOR](ns-strmini-_hw_event_descriptor.md) | When the class driver calls one of the minidriver's StrMiniEvent routines, it passes a pointer to an HW_EVENT_DESCRIPTOR structure to describe the event as enabled or disabled. |
| [_HW_STREAM_DESCRIPTOR](ns-strmini-_hw_stream_descriptor.md) | The minidriver uses the HW_STREAM_DESCRIPTOR structure to return stream information to the stream class driver. |
| [_HW_STREAM_HEADER](ns-strmini-_hw_stream_header.md) | The HW_STREAM_HEADER structure describes the kernel streaming semantics supported by the minidriver as a whole, as part of a HW_STREAM_DESCRIPTOR structure. |
| [_HW_STREAM_INFORMATION](ns-strmini-_hw_stream_information.md) | The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an HW_STREAM_DESCRIPTOR structure. |
| [_HW_STREAM_OBJECT](ns-strmini-_hw_stream_object.md) | HW_STREAM_OBJECT describes an instance of a minidriver stream. |
| [_HW_STREAM_REQUEST_BLOCK](ns-strmini-_hw_stream_request_block.md) | The stream class driver uses the HW_STREAM_REQUEST_BLOCK structure to pass information to and from the minidriver, using minidriver provided callbacks. |
| [_HW_TIME_CONTEXT](ns-strmini-_hw_time_context.md) | The class driver passes an HW_TIME_CONTEXT structure as a parameter to be filled in by a stream's StrMiniClock routine, or returns a completed HW_TIME_CONTEXT structure when it responds to a StreamClassQueryMasterClock or StreamClassQueryMasterClockSync request. |
| [_STREAM_DATA_INTERSECT_INFO](ns-strmini-_stream_data_intersect_info.md) | STREAM_DATA_INTERSECT_INFO describes the parameters of a data intersection operation. |
| [_STREAM_METHOD_DESCRIPTOR](ns-strmini-_stream_method_descriptor.md) | . |
| [_STREAM_PROPERTY_DESCRIPTOR](ns-strmini-_stream_property_descriptor.md) | STREAM_PROPERTY_DESCRIPTOR specifies the parameters of property get/set requests that the class driver passes to the minidriver. |
| [_STREAM_TIME_REFERENCE](ns-strmini-_stream_time_reference.md) | . |
| [KSSCATTER_GATHER](ns-strmini-ksscatter_gather.md) | . |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_SRB_COMMAND](ne-strmini-_srb_command.md) | . |
| [_STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE](ne-strmini-_stream_minidriver_device_notification_type.md) | . |
| [_STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE](ne-strmini-_stream_minidriver_stream_notification_type.md) | . |
| [_STREAM_PRIORITY](ne-strmini-_stream_priority.md) | TD. |
| [STREAM_BUFFER_TYPE](ne-strmini-stream_buffer_type.md) | This enumeration defines the buffer types for StreamClassGetPhysicalAddress. |
| [STREAM_DEBUG_LEVEL](ne-strmini-stream_debug_level.md) | The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output. |
| [TIME_FUNCTION](ne-strmini-time_function.md) | . |