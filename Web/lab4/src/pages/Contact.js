import React, { useState } from 'react';
import './Contact.css';

function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });

  const [submitted, setSubmitted] = useState(false);
  const [errors, setErrors] = useState({});

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.name.trim()) {
      newErrors.name = 'Name is required';
    }
    
    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }
    
    if (!formData.subject.trim()) {
      newErrors.subject = 'Subject is required';
    }
    
    if (!formData.message.trim()) {
      newErrors.message = 'Message is required';
    }
    
    return newErrors;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
    // Clear error for this field when user starts typing
    if (errors[name]) {
      setErrors(prevErrors => ({
        ...prevErrors,
        [name]: ''
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const newErrors = validateForm();
    
    if (Object.keys(newErrors).length === 0) {
      setSubmitted(true);
      setFormData({
        name: '',
        email: '',
        subject: '',
        message: ''
      });
      
      // Hide success message after 5 seconds
      setTimeout(() => setSubmitted(false), 5000);
    } else {
      setErrors(newErrors);
    }
  };

  const contactInfo = [
    {
      id: 1,
      icon: '📧',
      title: 'Email',
      details: 'support@edulearn.com',
      description: 'Send us an email anytime'
    },
    {
      id: 2,
      icon: '📱',
      title: 'Phone',
      details: '+1 (555) 123-4567',
      description: 'Call us during business hours'
    },
    {
      id: 3,
      icon: '📍',
      title: 'Address',
      details: '123 Education Way, Tech City, TC 12345',
      description: 'Visit our office'
    },
    {
      id: 4,
      icon: '🕐',
      title: 'Business Hours',
      details: 'Mon - Fri: 9AM - 6PM',
      description: 'Weekend support available'
    }
  ];

  return (
    <main className="contact">
      <div className="contact-hero">
        <h1>Get In Touch</h1>
        <p>Have questions? We'd love to hear from you</p>
      </div>

      <div className="contact-container">
        <section className="contact-info-section">
          <h2>Contact Information</h2>
          <div className="contact-info-grid">
            {contactInfo.map(info => (
              <div key={info.id} className="contact-info-card">
                <div className="info-icon">{info.icon}</div>
                <h3>{info.title}</h3>
                <p className="info-details">{info.details}</p>
                <p className="info-description">{info.description}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="contact-form-section">
          <h2>Send us a Message</h2>
          
          {submitted && (
            <div className="success-message">
              ✓ Thank you! Your message has been sent successfully. We'll get back to you soon!
            </div>
          )}

          <form onSubmit={handleSubmit} className="contact-form">
            <div className="form-group">
              <label htmlFor="name">Name *</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Your full name"
                className={errors.name ? 'error' : ''}
              />
              {errors.name && <span className="error-message">{errors.name}</span>}
            </div>

            <div className="form-group">
              <label htmlFor="email">Email *</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="your.email@example.com"
                className={errors.email ? 'error' : ''}
              />
              {errors.email && <span className="error-message">{errors.email}</span>}
            </div>

            <div className="form-group">
              <label htmlFor="subject">Subject *</label>
              <input
                type="text"
                id="subject"
                name="subject"
                value={formData.subject}
                onChange={handleChange}
                placeholder="What is this about?"
                className={errors.subject ? 'error' : ''}
              />
              {errors.subject && <span className="error-message">{errors.subject}</span>}
            </div>

            <div className="form-group">
              <label htmlFor="message">Message *</label>
              <textarea
                id="message"
                name="message"
                value={formData.message}
                onChange={handleChange}
                placeholder="Your message here..."
                rows="6"
                className={errors.message ? 'error' : ''}
              ></textarea>
              {errors.message && <span className="error-message">{errors.message}</span>}
            </div>

            <button type="submit" className="submit-button">Send Message</button>
          </form>
        </section>
      </div>

      <section className="faq-section">
        <h2>Frequently Asked Questions</h2>
        <div className="faq-grid">
          <div className="faq-item">
            <h3>How can I enroll in a course?</h3>
            <p>Visit our Courses page, select your desired course, and click "Enroll Now". You'll need to create an account to get started.</p>
          </div>
          <div className="faq-item">
            <h3>Do I get a certificate?</h3>
            <p>Yes! You'll receive a certificate upon successful completion of any course. Certificates are recognized by industry professionals.</p>
          </div>
          <div className="faq-item">
            <h3>Can I get a refund?</h3>
            <p>We offer a 30-day money-back guarantee if you're not satisfied with a course.</p>
          </div>
          <div className="faq-item">
            <h3>How long do I have access?</h3>
            <p>Once enrolled, you have lifetime access to course materials, so you can learn at your own pace whenever you want.</p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default Contact;
